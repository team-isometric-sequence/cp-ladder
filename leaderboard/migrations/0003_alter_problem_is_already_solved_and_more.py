# Generated by Django 4.2.7 on 2024-03-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_remove_problem_is_solved_problem_is_solvable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='is_already_solved',
            field=models.BooleanField(default=False, verbose_name='이미 해결한 문제인지 여부'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='is_solved_bt_yonsei',
            field=models.BooleanField(default=False, verbose_name='연세대학교 학생이 해결한 문제인지 여부'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='is_solved_by_ehwa',
            field=models.BooleanField(default=False, verbose_name='이화여자대학교 학생이 해결한 문제인지 여부'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='is_solved_by_hongik',
            field=models.BooleanField(default=False, verbose_name='홍익대학교 학생이 해결한 문제인지 여부'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='is_solved_by_sogang',
            field=models.BooleanField(default=False, verbose_name='서강대학교 학생이 해결한 문제인지 여부'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='is_solved_by_sookmyeong',
            field=models.BooleanField(default=False, verbose_name='숙명여자대학교 학생이 해결한 문제인지 여부'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='solved_count',
            field=models.IntegerField(default=0, verbose_name='해결한 사람 수'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='submission_count',
            field=models.IntegerField(default=0, verbose_name='제출 수'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='문제 난이도'),
        ),
    ]
