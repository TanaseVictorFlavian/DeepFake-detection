import os
from name_creator import name_creator
import shutil

class DatasetCreator:
    def __init__(self, in_pos_paths : list, 
                in_neg_paths : list, 
                out_pos_path : str, 
                out_neg_path : str):   
        """
        :param in_pos_path: Path to the input positive samples
        :param in_neg_path: Path to the input negative samples
        :param out_pos_path: Path to the output positive samples
        :param out_neg_path: Path to the output negative samples
        """

        self.check_in_path(in_pos_paths + in_neg_paths)
        self.check_out_paths(out_neg_path + out_pos_path)

        for path in out_neg_path + out_pos_path:
            # QOL for users
            if path[-1] != "/":
                path += "/"

        self.pos_paths = in_pos_paths
        self.neg_paths = in_neg_paths
        self.out_pos_paths = out_pos_path
        self.out_neg_paths = out_neg_path

    def check_in_paths(self, paths : list):
        # Check for the existance of the paths 
        for path in paths:
            if not os.path.exists(path):
                print(f"{path} does not exist.")
                exit(1)

    def check_out_paths(self, paths : list):   
        # Check for the existance of the paths 
        for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Created dir at {path}")

    def fetch_data(self, path, label : str):
        file_counter = len(os.listdir(path)) 
        for file in os.listdir(path):
            file_counter += 1
            if file.endswith(".png") or file.endswith(".jpg"):
                if label == "pos": 
                    shutil.copy2(path + file, self.out_pos_path + name_creator(file_counter) + ".png")
                else:
                    shutil.copy2(path + file, self.out_neg_path + name_creator(file_counter) + ".png") 

