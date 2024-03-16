# Generated by Django 4.2.7 on 2024-03-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='is_solved',
        ),
        migrations.AddField(
            model_name='problem',
            name='is_solvable',
            field=models.BooleanField(default=False, verbose_name='풀이 가능한지 여부'),
        ),
    ]
