from utils.Classes.DatasetCreator import DatasetCreator
import os 


if __name__ == "__main__":
    # Define the paths for the dataset creator
    ROOT_IN_DIR = "../ExtractedFaces/"
    ROOT_OUT_DIR = "./data/"
    in_pos_paths = [f"{ROOT_IN_DIR}Celeb-real/", f"{ROOT_IN_DIR}YouTube-real/"]
    in_neg_paths = [ROOT_IN_DIR + "Forensics_pp/" + dir + "/" for dir in os.listdir(f"{ROOT_IN_DIR}Forensics_pp/")] # + [f"{ROOT_IN_DIR}CelebDF/"]
    out_pos_path = f"{ROOT_OUT_DIR}Positive_images/"
    out_neg_path = f"{ROOT_OUT_DIR}Negative_images/"

    creator = DatasetCreator(in_pos_paths, in_neg_paths, out_pos_path, out_neg_path)   
    creator.create_dataset()  