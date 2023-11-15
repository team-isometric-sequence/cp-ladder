from typing import Optional

from core.models import Directory, HostedFile, FileDto, DirectoryDto


class AddDirectoryEntry:
    @classmethod
    def call(cls, parent: Optional[Directory], dto: DirectoryDto) -> Directory:
        directory = Directory(parent=parent, name=dto.name)
        directory.save()

        return directory
        
class AddFileEntry:
    @classmethod
    def call(cls, directory: Optional[Directory], dto: FileDto) -> HostedFile:
        hosted_file = HostedFile(parent=directory, name=dto.name)
        hosted_file.save()

        return hosted_file

