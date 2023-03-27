from IndexCreator.index_creator import IndexCreator
import sys
import os

if __name__ == "__main__":
    path_to_dir = sys.argv[1]
    creator = IndexCreator(sys.argv[2])
    creator.create_indexes(path_to_dir)