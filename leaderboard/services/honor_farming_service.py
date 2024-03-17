from django.db.models import QuerySet

from leaderboard.models import BojUser, Problem, ProblemFilterType, ProblemSolver, Tagging

from leaderboard.services import categorization_service


def list_problems() -> QuerySet[Problem]:
    return Problem.objects.all()


def list_unsolved_problems(params: ProblemFilterType) -> QuerySet[Problem]:
    allow_unranked = params.get('allow_unranked', False)
    school = params.get('school', '')
    tag_name = params.get('tag_name', '')

    query = _filter_by_school(school)
    query = _filter_by_tag(query, tag_name)

    query = query if allow_unranked else query.filter(tier__gt=0)

    query = query.order_by(*generate_filter_option(params))

    return query

def _filter_by_school(school):
    problems = Problem.objects.filter(is_solvable=True)

    if school == 'hongik':
        return problems.filter(is_solved_by_hongik=False)
    if school == 'ehwa':
        return problems.filter(is_solved_by_ehwa=False)
    if school == 'sogang': 
        return problems.filter(is_solved_by_sogang=False)
    if school == 'yonsei': 
        return problems.filter(is_solved_by_yonsei=False)
    if school == 'sookmyeong': 
        return problems.filter(is_solved_by_sookmyeong=False)

    return problems

def _filter_by_tag(query: QuerySet[Problem], tag_name):
    if tag_name == '': 
        return query 

    tag = categorization_service.find_or_create_tag(tag_name)

    taggings = Tagging.objects.filter(tag=tag)
    problem_ids = [tagging.problem_id for tagging in taggings]
    return query.filter(id__in=problem_ids)

def generate_filter_option(params: ProblemFilterType) -> list[str]:
    order_by = params.get('order_by', '')

    if order_by == 'tier_asc': 
        return ['tier']
    if order_by == 'tier_desc': 
        return ['-tier']
    if order_by == 'solved_count_asc': 
        return ['solved_count']
    if order_by == 'solved_count_desc': 
        return ['-solved_count']
    if order_by == 'submission_count_asc': 
        return ['submission_count']

    return ['tier']


def get_problem(boj_problem_id: int) -> Problem:
    problem, _ = Problem.objects.get_or_create(problem_number=boj_problem_id)
    return problem


def get_boj_user(boj_handle: str) -> BojUser:
    user, _ = BojUser.objects.get_or_create(boj_handle=boj_handle)
    return user


def get_problem_solver(problem_id: int, boj_user_id: int) -> ProblemSolver:
    problem = get_problem(problem_id)
    solver, _ = ProblemSolver.objects.get_or_create(problem_id=problem.pk, boj_user_id=boj_user_id)
    return solver


def update_problem(problem: Problem, **kwargs) -> Problem:
    for key, value in kwargs.items():
        setattr(problem, key, value)
    problem.save()
    return problem
