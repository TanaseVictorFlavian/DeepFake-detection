from utils import DatasetCreator
import os 


if __name__ == "__main__":
    # Define the paths for the dataset creator

    in_pos_paths = ["../ExtractedFaces/Celeb-real/", "../ExtractedFaces/YouTube-real/"]
    in_neg_paths = [dir for dir in os.listdir("../ExtractedFaces/Forensics_pp/")] + ["../ExtractedFaces/CelebDF/"]
    out_pos_path = "/data/Positive_images/"
    out_neg_path = "./data/Negative_images/"

    creator = DatasetCreator(in_pos_paths, in_neg_paths, out_pos_path, out_neg_path)