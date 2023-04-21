import unittest

from tools.index_creator import IndexCreator


class IndexCreatorTest(unittest.TestCase):

    def test_CheckIndexCreator_SplitTrue(self):

        code = ["public class Main {",
                "    public static void main(String[] args) {",
                "        System.out.println('Hello, world!');",
                "    }",
                "}"]

        path_to_file = "../resources/source_code_to_index/generated-code/small_code/code.java"
        with open(path_to_file, 'w') as file:
            for line in code:
                file.writelines(line + '\n')

        index = {"public": {path_to_file: 2},
                 "class": {path_to_file: 1},
                 "Main": {path_to_file: 1},
                 "static": {path_to_file: 1},
                 "void": {path_to_file: 1},
                 "main": {path_to_file: 1},
                 "String": {path_to_file: 1},
                 "args": {path_to_file: 1},
                 "System": {path_to_file: 1},
                 "out": {path_to_file: 1},
                 "println": {path_to_file: 1},
                 'Hello': {path_to_file: 1},
                 'world': {path_to_file: 1}}

        save_path = "../resources/test/inverted_indexes/"
        path_to_dir = "../resources/source_code_to_index/generated-code/"
        path_to_index = "../resources/test/inverted_indexes/small_code.json"

        creator = IndexCreator()
        creator.set_save_directory(save_path)
        creator.create_indexes(path_to_dir)
        generated_index = IndexCreator.read_index_from_file(path_to_index)

        self.assertEqual(index, generated_index)

    def test_CheckIndexCreator_SplitFalse(self):

        code = ["public class Main {",
                "    public static void main(String[] args) {",
                "        System.out.println('Hello, world!');",
                "    }",
                "}"]

        path_to_file = "../resources/source_code_to_index/generated-code/small_code/code.java"
        with open(path_to_file, 'w') as file:
            for line in code:
                file.writelines(line + '\n')

        index = {"public": {path_to_file: 2},
                 "class": {path_to_file: 1},
                 "Main": {path_to_file: 1},
                 "static": {path_to_file: 1},
                 "void": {path_to_file: 1},
                 "main": {path_to_file: 1},
                 "String": {path_to_file: 1},
                 "args": {path_to_file: 1},
                 "System": {path_to_file: 1},
                 "out": {path_to_file: 1},
                 "println": {path_to_file: 1},
                 'Hello': {path_to_file: 1},
                 'world': {path_to_file: 1}}

        save_path = "../resources/test/inverted_indexes/"
        path_to_dir = "../resources/source_code_to_index/generated-code/small_code"
        path_to_index = "../resources/test/inverted_indexes/small_code.json"

        creator = IndexCreator()
        creator.set_save_directory(save_path)
        creator.create_indexes(path_to_dir, split=False)
        generated_index = IndexCreator.read_index_from_file(path_to_index)

        self.assertEqual(index, generated_index)
