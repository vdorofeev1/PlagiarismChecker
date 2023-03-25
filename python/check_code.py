from CodeChecker.code_checker import CodeChecker
import sys

if __name__ == "__main__":
    if sys.argv[1] == "ping":
        print("alive")
    else:
        checker = CodeChecker()
        checker.create_tokens(sys.argv[1])
        print(checker.check_code())
