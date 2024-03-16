from leaderboard.models import Problem, Tag, Tagging


def get_tag(tag_name: str) -> Tag:
    tag, _ = Tag.objects.get_or_create(name=tag_name)
    return tag


def get_tagging(tag: Tag, problem: Problem) -> Tagging:
    tagging, _ = Tagging.objects.get_or_create(tag=tag, problem=problem)
    return tagging


def add_to_problem(tag_name: str, problem: Problem):
    tag = get_tag(tag_name)
    tagging = get_tagging(tag, problem)

    tagging.tag_name = tag_name
    tagging.save()


def update_tagging(tagging: Tagging, **kwargs) -> Tagging:
    for key, value in kwargs.items():
        setattr(tagging, key, value)
    tagging.save()
    return tagging

