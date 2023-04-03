import unittest

from tools.code_checker import CodeChecker


class CodeCheckerTest(unittest.TestCase):
    path_to_index_dir = "../resources/test/inverted_indexes"

    def test_CodeChecker_returnFile(self):
        path_to_file = "../resources/test/check_code/Main.java"
        checker = CodeChecker(CodeCheckerTest.path_to_index_dir)
        checker.create_tokens(path_to_file)
        self.assertEqual(checker.check_code(), False)

    def test_CodeChecker_returnOK(self):
        path_to_file = "../resources/test/check_code/ExampleHealthIndicator.java"
        checker = CodeChecker(CodeCheckerTest.path_to_index_dir)
        checker.create_tokens(path_to_file)
        self.assertEqual(checker.check_code(), True)
