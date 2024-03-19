from utils.Classes.DatasetCreator import DatasetCreator
from utils.Classes.ImageDataset import ImageDataset
from utils.name_creator import name_creator
import os 
import shutil

if __name__ == "__main__":  
    neg_root = "../ExtractedFaces/Negatives/"
    pos_root = "../ExtractedFaces/Positives/"
    pos_out = "./data/Positves/"
    neg_out = "./data/Negatives/"
    
    datasets = [
        ImageDataset(f"{neg_root}CelebDF/", "neg", 2),
        ImageDataset(f"{neg_root}Forensicspp/Deepfakes/", "neg", 2),
        ImageDataset(f"{neg_root}Forensicspp/Face2Face/", "neg", 2),
        ImageDataset(f"{neg_root}Forensicspp/FaceSwap/", "neg", 2),
        ImageDataset(f"{neg_root}Forensicspp/NeuralTextures/", "neg", 2),
        ImageDataset(f"{neg_root}Forensicspp/FaceShifter/", "neg", 2),
        ImageDataset(f"{pos_root}Celeb-real/", "pos", 10),
        ImageDataset(f"{pos_root}Youtube-real/", "pos", 10)
    ]

    junk = [ImageDataset(f"{neg_root}junk_negative/", "neg"), 
            ImageDataset(f"{pos_root}junk_positive/", "pos"), 
            ImageDataset(f"{pos_root}Forensics_youtube/", "pos")]
    
    ds_creator = DatasetCreator(datasets, junk)
    ds_creator.create_train_test()