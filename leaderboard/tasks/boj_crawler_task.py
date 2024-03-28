from time import sleep
from itertools import islice, chain
import requests

from leaderboard.models import Problem
import leaderboard.services.honor_farming_service as honor_farming_service


def batch(iterable, size):
    l = len(iterable)
    for ndx in range(0, l, size):
        yield iterable[ndx:min(ndx + size, l)]

def crawl_problems():
    for page in range(1,501):
        sleep(0.4)
        path = f"https://solved.ac/api/v3/search/problem?query=+&page={page}&sort=id&direction=asc"
        response = requests.get(path)
        print(path)
        if response.status_code != 200:
            continue

        data = response.json()
        if len(data['items']) == 0:
            break

        problem_numbers = [ int(problem['problemId']) for problem in data['items']]
        honor_farming_service.get_problems(problem_numbers)


def crawl_school(school: str):
    school_id = _get_school_id(school)
    for page in range(1, 200):
        sleep(1.0)
        path = f"https://solved.ac/api/v3/ranking/in_organization?organizationId={school_id}&page={page}"
        print(path)
        response = requests.get(path)
        if response.status_code != 200:
            print(response.status_code)
            break

        data = response.json()
        if len(data['items']) == 0:
            break

        users = [user['handle'] for user in data['items']]
        for username in users:
            sleep(1)

            boj_user = honor_farming_service.get_boj_user(username)
            solved_problem_numbers = []

            for i in range(1, 300):
                sleep(0.4)
                url = f"https://solved.ac/api/v3/search/problem?query=solved_by:{username}&page={i}"
                response = requests.get(url)
                if response.status_code != 200:
                    break

                data = response.json()
                if len(data['items']) == 0:
                    break

                problem_numbers = [ int(problem['problemId']) for problem in data['items']]
                problems = honor_farming_service.get_problems(problem_numbers)
                solved_problem_numbers = [*solved_problem_numbers, *[problem.problem_number for problem in problems ]]
                
            for chunk in batch(solved_problem_numbers, 100):
                solved_problem_ids = list(chunk)

                # TODO: Raises IntegrationError
                # honor_farming_service.get_problem_solvers(solved_problem_ids, boj_user.pk)

                Problem.objects.filter(problem_number__in=solved_problem_ids).update(**{_get_school_related_field(school): True, 'is_already_solved': True})


def _get_school_id(school: str) -> int:
    if school == '홍익대학교':
        return 436
    if school == '이화여자대학교':
        return 352
    if school == '서강대학교':
        return 292
    if school == '연세대학교':
        return 331
    if school == '숙명여자대학교':
        return 319

    return 0


def _get_school_related_field(school):
    if school == '홍익대학교':
        return 'is_solved_by_hongik'
    if school == '이화여자대학교':
        return 'is_solved_by_ehwa'
    if school == '서강대학교': 
        return 'is_solved_by_sogang'
    if school == '연세대학교': 
        return 'is_solved_by_yonsei' 
    if school == '숙명여자대학교': 
        return 'is_solved_by_sookmyeong'
    return 'is_already_solved'

