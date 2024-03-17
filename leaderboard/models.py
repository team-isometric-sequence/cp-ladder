from typing import TypedDict
from django.db import models


class ProblemFilterType(TypedDict):
    allow_unranked: bool
    school: str 
    tag_name: str
    order_by: str


class BojUser(models.Model):
    boj_handle = models.TextField(max_length=256, verbose_name="BOJ 핸들")

    class Meta:
        verbose_name = 'boj user'
        verbose_name_plural = 'boj users'

        db_table = 'boj_users'


class Tag(models.Model):
    name = models.TextField(max_length=256, verbose_name="태그 이름")

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

        db_table = 'tags'

class Tagging(models.Model):
    problem = models.ForeignKey("Problem", on_delete=models.CASCADE, verbose_name="문제")
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, verbose_name="태그")
    tag_name = models.TextField(max_length=256, verbose_name="태그 이름")

    class Meta:
        verbose_name = 'tagging'
        verbose_name_plural = 'taggings'

        db_table = 'taggings'


class ProblemSolver(models.Model):
    problem = models.ForeignKey("Problem", on_delete=models.CASCADE, verbose_name="문제")
    boj_user = models.ForeignKey("BojUser", on_delete=models.CASCADE, verbose_name="BOJ 사용자")

    class Meta:
        verbose_name = 'problem solver'
        verbose_name_plural = 'problem solvers'

        db_table = 'problem_solvers'
    

class Problem(models.Model):
    title = models.TextField(max_length=256, verbose_name="문제 이름")
    problem_number = models.IntegerField(verbose_name="문제 번호")
    tier = models.IntegerField(verbose_name="문제 난이도", default=0)

    solved_count = models.IntegerField(verbose_name="해결한 사람 수", default=0)
    submission_count = models.IntegerField(verbose_name="제출 수", default=0)

    is_solvable = models.BooleanField(verbose_name="풀이 가능한지 여부", default=False,)
    is_already_solved = models.BooleanField(verbose_name="이미 해결한 문제인지 여부", default=False)
    
    is_solved_by_hongik = models.BooleanField(verbose_name="홍익대학교 학생이 해결한 문제인지 여부", default=False)
    is_solved_by_ehwa = models.BooleanField(verbose_name="이화여자대학교 학생이 해결한 문제인지 여부", default=False)
    is_solved_by_sogang = models.BooleanField(verbose_name="서강대학교 학생이 해결한 문제인지 여부", default=False)
    is_solved_by_yonsei = models.BooleanField(verbose_name="연세대학교 학생이 해결한 문제인지 여부", default=False)
    is_solved_by_sookmyeong = models.BooleanField(verbose_name="숙명여자대학교 학생이 해결한 문제인지 여부", default=False)

    created_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="생성 시간")
    updated_at = models.DateTimeField(blank=True, auto_now=True, verbose_name="수정 시간")

    tags = models.ManyToManyField("Tag", through="Tagging", verbose_name="태그")

    @property 
    def tag_names(self):
        return list(self.tags.values_list('name', flat=True))

    @property 
    def badge_asset_path(self):
        return f'badges/{self.tier}.svg'

    class Meta:
        verbose_name = 'problem'
        verbose_name_plural = 'problems'

        db_table = 'problems'
