import unittest

from CodeChecker.code_checker import CodeChecker


class CodeCheckerTest(unittest.TestCase):
    path_to_index_dir = "/home/vdorofeev/PlagiarismChecker/python/resources/inverted_indexes"

    def test_CodeChecker_returnFile(self):
        path_to_file = "/home/vdorofeev/MyProjects/ufi/core/ufi-client/src/main/java/net/iponweb/ufi/api/client/v6/AddHintsRequest.java"
        checker = CodeChecker(CodeCheckerTest.path_to_index_dir)
        checker.create_tokens(path_to_file)
        self.assertEqual(checker.check_code(), False)

    def test_CodeChecker_returnOK(self):
        path_to_file = "/home/vdorofeev/PlagiarismChecker/python/resources/source_code/spring-boot/spring-boot-tests/" \
                       "spring-boot-smoke-tests/spring-boot-smoke-test-actuator/src/main/java/smoketest/actuator/ExampleHealthIndicator.java"
        checker = CodeChecker(CodeCheckerTest.path_to_index_dir)
        checker.create_tokens(path_to_file)
        self.assertEqual(checker.check_code(), True)
