import uuid
from dataclasses import dataclass

from django.db import models

# Create your models here.

class VNode(models.Model):
    node_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, verbose_name="노드 ID") 
    name = models.TextField(max_length=256, verbose_name="디렉토리 / 파일 이름")

    created_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="생성 시간")
    updated_at = models.DateTimeField(blank=True, auto_now=True, verbose_name="수정 시간")

    parent = models.ForeignKey("core.Directory", null=True, on_delete=models.DO_NOTHING, verbose_name="부모 디렉토리", related_name="children")


class Directory(VNode):
    class Meta:
        verbose_name = 'directory'
        verbose_name_plural = 'directories'

        db_table = 'directories'


class HostedFile(VNode):
    class Meta:
        verbose_name = 'file'
        verbose_name_plural = 'files'

        db_table = 'hosted_files'



@dataclass
class FileDto:
    name: str


@dataclass
class DirectoryDto:
    name: str
