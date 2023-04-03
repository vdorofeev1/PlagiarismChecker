import os
import pickle

from pygments import lex
from pygments.lexers import JavaLexer
from pygments.token import Keyword, Name


class IndexCreator:
    lexer = JavaLexer()

    def __init__(self, save_directory):
        self.__files = []
        self.__inverted_index = {}
        self.__count = 0
        self.__save_directory = save_directory

    def __find_files(self, path_to_dir):
        files = []
        for dirpath, dirnames, filenames in os.walk(path_to_dir):
            for filename in filenames:
                if filename.endswith('.java'):
                    files.append(os.path.join(dirpath, filename))
                    self.__count += 1
        return files

    @DeprecationWarning
    def create_index_deprecated(self, path_to_dir):
        self.__files = self.__find_files(path_to_dir)
        # inverted_index = defaultdict(lambda: defaultdict(int)) //can`t save it to file
        inverted_index = {}
        for file in self.__files:
            with open(file, 'r') as f:
                source_code = f.read()
            lexer = JavaLexer()
            # formatter = RawTokenFormatter()                // sorry...
            tokens = lex(source_code, lexer)
            for token in tokens:
                token_type = token[0]
                token_value = token[1]
                if token_type in Keyword or token_type in Name:
                    if token_value not in inverted_index.keys():
                        inverted_index[token_value] = {}
                    if file not in inverted_index[token_value].keys():
                        inverted_index[token_value][file] = 1
                    else:
                        inverted_index[token_value][file] += 1

        self.__inverted_index = inverted_index

    def __add_to_index(self, tokens, file):
        for token in tokens:
            token_type = token[0]
            token_value = token[1]
            if token_type in Keyword or token_type in Name:
                if token_value not in self.__inverted_index.keys():
                    self.__inverted_index[token_value] = {}
                if file not in self.__inverted_index[token_value].keys():
                    self.__inverted_index[token_value][file] = 1
                else:
                    self.__inverted_index[token_value][file] += 1

    def create_indexes(self, path_to_directory):
        for directory in os.listdir(path_to_directory):
            for file in self.__find_files(os.path.join(path_to_directory, directory)):
                tokens = IndexCreator.create_tokens(file)
                self.__add_to_index(tokens, file)
            self.__save_index_to_file(self.__save_directory + directory + ".json")
            self.__inverted_index.clear()

    def __save_index_to_file(self, path_to_file):
        with open(path_to_file, 'wb') as f:
            pickle.dump(self.__inverted_index, f)

    @staticmethod
    def read_index_from_file(path_to_file):
        with open(path_to_file, 'rb') as f:
            inverted_index = pickle.load(f)
        return inverted_index

    @staticmethod
    def create_tokens(file):
        try:
            with open(file, 'r') as f:
                source_code = f.read()
            return lex(source_code, IndexCreator.lexer)
        except UnicodeError:
            print(f"Can`t read this file: {file}")
            return []

    def get_index(self):
        return self.__inverted_index

