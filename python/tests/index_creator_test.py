import unittest

from pygments.token import Keyword, Name

from tools.index_creator import IndexCreator


class IndexCreatorTest(unittest.TestCase):

    def test_CheckIndexCreator(self):

        code = ["public class Main {",
                "    public static void main(String[] args) {",
                "        System.out.println('Hello, world!');",
                "    }",
                "}"]

        path_to_file = "../resources/source_code_to_index/generated-code/small_code/code.java"
        with open(path_to_file, 'w') as file:
            for line in code:
                file.writelines(line + '\n')


        index = {"public": {"../resources/source_code_to_index/generated-code/small_code/code.java": 2},
                 "class": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 "Main": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 "static": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 "void": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 "main": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 "String": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 "args": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 "System": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 "out": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 "println": {"../resources/source_code_to_index/generated-code/small_code/code.java": 1},
                 'Hello': {'../resources/source_code_to_index/generated-code/small_code/code.java': 1},
                 'world': {'../resources/source_code_to_index/generated-code/small_code/code.java': 1}}


        save_path = "../resources/test/inverted_indexes/"
        path_to_dir = "../resources/source_code_to_index/generated-code/"
        path_to_index = "../resources/test/inverted_indexes/small_code.json"

        creator = IndexCreator(save_path)
        creator.create_indexes(path_to_dir)
        generated_index = IndexCreator.read_index_from_file(path_to_index)

        self.assertEqual(index, generated_index)

