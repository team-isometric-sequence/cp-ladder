from typing import TypedDict
from time import sleep
from operator import itemgetter

import requests

from leaderboard.services import honor_farming_service, categorization_service


class TagSchema(TypedDict):
    key: str


class ProblemMetric(TypedDict):
    problemId: int
    level: int
    titleKo: str
    acceptedUserCount: int 
    averageTries: float 
    isSolavable: bool 
    tags: list[TagSchema]


def crawl_solvedac_tiers():
    problems = honor_farming_service.list_problems()
    problems = problems.order_by('tier')

    page_size = 100 
    total_pages = (problems.count() + page_size - 1) // page_size

    for page in range(1, total_pages + 1):
        chunk = problems[(page - 1) * page_size: page * page_size]

        problem_ids: list[str] = [*map(str, chunk.values_list('problem_number', flat=True))]
        query_string: str = ','.join(problem_ids)

        update_solvedac_metric(query_string)


def update_solvedac_metric(query_string: str):
    sleep(0.2)
    url = f"https://solved.ac/api/v3/problem/lookup?problemIds={query_string}"

    response = requests.get(url)
    if response.status_code != 200:
        return

    metrics: list[ProblemMetric] = response.json()
    for metric in metrics:
        # Bypasses destructuring assignment
        problem_id, level, title, solved_count, submission_rate, tags = itemgetter('problemId', 'level', 'titleKo', 'acceptedUserCount', 'averageTries', 'tags')(metric)
        problem = honor_farming_service.get_problem(problem_id)
         
        data = { 
            'title': title,
            'tier': level,
            'is_solvable': True if solved_count > 0 else False,
            'solved_count': solved_count,
            'submission_count': round(solved_count * submission_rate),
        }     

        honor_farming_service.update_problem(problem, **data)
        for t in tags:
            tag = categorization_service.get_tag(t['key'])
            tagging = categorization_service.get_tagging(tag, problem)
            categorization_service.update_tagging(tagging, tag_name=t['key'])

