import unittest

from pygments.token import Keyword, Name

from tools.index_creator import IndexCreator


class IndexCreatorTest(unittest.TestCase):
    def test_IndexCreator(self):
        path = "/home/vdorofeev/MyProjects/ufi/core/ufi-core/src"
        save_path = "/home/vdorofeev/MyProjects/test_project_for_jb/file.json"
        creator = IndexCreator(save_path)
        creator.create_index_deprecated(path)
        creator.save_index_to_file(save_path)
        self.assertEqual(creator.get_index(), creator.read_index_from_file(save_path))

    def test_newIndexCreator(self):
        path = "/home/vdorofeev/PlagiarismChecker/python/resources/source_code/generated-code"
        save = "/home/vdorofeev/PlagiarismChecker/python/resources/inverted_indexes/"
        creator = IndexCreator(save)
        creator.create_indexes(path)

    def test_CheckIndexCreator(self):
        save_path = "../resources/inverted_indexes/"
        creator = IndexCreator(save_path)
        file = "../resources/source_code/generated-code/small_code/code.java"
        tokens = IndexCreator.create_tokens(file)
        index = {}
        for token in tokens:
            token_type = token[0]

            token_value = token[1]

            if token_type in Keyword or token_type in Name:
                print(token_value)
                if token_value not in index.keys():
                    index[token_value] = {}
                if file not in index[token_value].keys():
                    index[token_value][file] = 1
                else:
                    index[token_value][file] += 1
            else:
                #print("NOT KEYWORD: ", token_value)
                pass


