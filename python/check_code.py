from tools.code_checker import CodeChecker
import sys
import os

if __name__ == "__main__":
    if sys.argv[1] == "ping":
        print("alive")
    else:
        path_to_file = sys.argv[1]
        path_to_index_dir = sys.argv[2]
        checker = CodeChecker(path_to_index_dir)
        checker.create_tokens(sys.argv[1])
        isSimilar = checker.check_code()
        if not isSimilar:
            print("OK")

