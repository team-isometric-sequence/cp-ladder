from typing import Optional
from leaderboard.models import Problem, Tag, Tagging


def get_tag(tag_name: str) -> Tag:
    tag, _ = Tag.objects.get_or_create(name=tag_name)
    return tag


def get_tagging(tag_id: int, problem_id: int) -> Tagging:
    tagging, _ = Tagging.objects.get_or_create(tag_id=tag_id, problem_id=problem_id)
    return tagging


def add_to_problem(tag_name: str, problem: Problem):
    tag = get_tag(tag_name)
    tagging = get_tagging(tag.pk, problem.pk)

    tagging.tag_name = tag_name
    tagging.save()


def update_tagging(tagging: Tagging, **kwargs) -> Tagging:
    for key, value in kwargs.items():
        setattr(tagging, key, value)
    tagging.save()
    return tagging

