from django.test import TestCase
from core.models import Directory, DirectoryDto

from core.services import AddDirectoryEntry


class FileSystemTestCase(TestCase):
    def __get_all_directories_from_root(self):
        return Directory.objects.filter(parent=None)

    def test_directory_hierarchy(self):
        a_directory = AddDirectoryEntry.call(None, DirectoryDto(name="a"))
        b_directory = AddDirectoryEntry.call(None, DirectoryDto(name="b"))
        AddDirectoryEntry.call(None, DirectoryDto(name="c"))

        d_directory = AddDirectoryEntry.call(a_directory, DirectoryDto(name="d"))
        AddDirectoryEntry.call(d_directory, DirectoryDto(name="e"))
                                             
        AddDirectoryEntry.call(b_directory, DirectoryDto(name="f"))
        AddDirectoryEntry.call(a_directory, DirectoryDto(name="g"))

        self.assertEqual(len(self.__get_all_directories_from_root()), 3)
        self.assertEqual(len(a_directory.children), 2)
