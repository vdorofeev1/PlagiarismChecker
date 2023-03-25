from IndexCreator.index_creator import IndexCreator
import sys

if __name__ == "__main__":
    creator = IndexCreator()
    path_to_dir = sys.argv[1]
    save_path = sys.argv[2]
    creator.create_index(path_to_dir)
    creator.save_index_to_file(save_path)