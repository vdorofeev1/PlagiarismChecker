import os
from collections import defaultdict

from pygments.token import Keyword, Name

from tools.index_creator import IndexCreator


class CodeChecker:
    def __init__(self, path_to_index_dir):
        self.__path_to_index_dir = path_to_index_dir
        self.__index = defaultdict(int)
        self.__total_count = 0

    def create_tokens(self, path_to_file):
        tokens = IndexCreator.create_tokens(path_to_file)
        for token in tokens:
            token_type = token[0]
            token_value = token[1]
            if token_type in Keyword or token_type in Name:
                self.__index[token_value] += 1
                self.__total_count += 1

    def check_code(self, ratio=0.85):
        isSimilar = False
        index_files = os.listdir(self.__path_to_index_dir)
        for index_file in index_files:
            inverted_index = IndexCreator.read_index_from_file(os.path.join(self.__path_to_index_dir, index_file))
            entry_count = defaultdict(int)
            for token_value, token_count in self.__index.items():
                if token_value in list(inverted_index.keys()):
                    for path, count in inverted_index[token_value].items():
                        entry_count[path] += min(token_count, count)

            max_count = 0
            repo_name = index_file[:index_file.find('.')]
            for path, count in entry_count.items():
                if max_count < count:
                    max_count = count
                    file_path = path
            if max_count / self.__total_count >= ratio:
                isSimilar = True
                print(f"Input file is similar to this file: {file_path[file_path.find(repo_name):]} in {repo_name}")
                print(f"Number of similar keywords: {max_count} ({(max_count / self.__total_count) * 100:.1f}%)")
        return isSimilar

    @DeprecationWarning
    def check_code_deprecated(self, ratio=0.85):
        inverted_index = IndexCreator.read_index_from_file(self.__path_to_index_dir)
        entry_count = defaultdict(int)

        for token_value, token_count in self.__index.items():
            if token_value in list(inverted_index.keys()):
                for path, count in inverted_index[token_value].items():
                    entry_count[path] += min(token_count, count)

        max_count = 0
        for path, count in entry_count.items():
            if max_count < count:
                max_count = count
                file_path = path
        print(max_count)
        print(self.__total_count)
        if (max_count / self.__total_count) >= ratio:
            return file_path
        else:
            return "OK"

