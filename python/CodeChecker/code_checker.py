from collections import defaultdict

from pygments import lex
from pygments.lexers import JavaLexer
from pygments.token import Keyword, Name

from IndexCreator.index_creator import IndexCreator


class CodeChecker:
    def __init__(self, path_to_index="../resources/inverted_indexes/file.json"):
        self.__path_to_index = path_to_index
        self.__index = {}
        self.__total_count = 0
        self.__path_to_file = ""

    def create_tokens(self, path_to_file):
        self.__path_to_file = path_to_file
        index = defaultdict(int)
        with open(self.__path_to_file, 'rb') as f:
            source_code = f.read()
        lexer = JavaLexer()
        tokens = lex(source_code, lexer)
        for token in tokens:
            token_type = token[0]
            token_value = token[1]
            if token_type in Keyword or token_type in Name:
                index[token_value] += 1
                self.__total_count += 1

        self.__index = index

    def check_code(self, ratio=0.85):
        inverted_index = IndexCreator.read_index_from_file(self.__path_to_index)
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
        if (max_count / self.__total_count) >= ratio:
            return file_path
        else:
            return "OK"
