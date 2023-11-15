# Generated by Django 4.2.7 on 2023-11-15 07:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VNode',
            fields=[
                ('node_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='노드 ID')),
                ('name', models.TextField(max_length=256, verbose_name='디렉토리 / 파일 이름')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 시간')),
            ],
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('vnode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.vnode')),
            ],
            options={
                'verbose_name': 'directory',
                'verbose_name_plural': 'directories',
                'db_table': 'directories',
            },
            bases=('core.vnode',),
        ),
        migrations.CreateModel(
            name='HostedFile',
            fields=[
                ('vnode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.vnode')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
                'db_table': 'hosted_files',
            },
            bases=('core.vnode',),
        ),
        migrations.AddField(
            model_name='vnode',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='core.directory', verbose_name='부모 디렉토리'),
        ),
    ]
