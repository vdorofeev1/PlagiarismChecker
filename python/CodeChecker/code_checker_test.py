import unittest

from CodeChecker.code_checker import CodeChecker
class MyTestCase(unittest.TestCase):

    def test_CodeChecker_returnFile(self):
        path1 = "/home/vdorofeev/MyProjects/ufi/core/ufi-core/src/main/java/net/iponweb/ufi/api/http/HttpConstants.java"
        checker = CodeChecker()
        checker.create_tokens(path1)
        self.assertEqual(checker.check_code(), path1)

    def test_CodeChecker_returnOK(self):
        path2 = "/home/vdorofeev/MyProjects/test_project_for_jb/java/ApiClient/src/main/java/com/vdorofeev/apiclient/ApiClientApplication.java"
        checker = CodeChecker()
        checker.create_tokens(path2)
        self.assertEqual(checker.check_code(), "OK")
