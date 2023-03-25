import unittest
from IndexCreator.index_creator import IndexCreator

class IndexCreatorTest(unittest.TestCase):
    def test_IndexCreator(self):
        path = "/home/vdorofeev/MyProjects/ufi/core/ufi-core/src"
        save_path = "/home/vdorofeev/MyProjects/test_project_for_jb/file.json"
        creator = IndexCreator()
        creator.create_index(path)
        creator.save_index_to_file(save_path)
        self.assertEqual(creator.get_index(), creator.read_index_from_file(save_path))

