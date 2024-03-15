import os
from multiprocessing import Process
"""
This script automates the face extraction from video sources.
It has a feature for the specific usecase when the user has to download 
the FaceForensics++ dataset beforehand.
"""

class VideoDataset:
    def __init__(self, name, in_root, out_root, subdirs = None, num_bins = 20, sample_size = 3):
        self.name = name
        self.root = in_root
        self.out_root = out_root
        self.num_bins = num_bins   
        self.sample_size = sample_size
        self.subdirs = subdirs
        self.out_paths = self.generate_out_paths()
    
    def generate_out_paths(self):
        if self.subdirs is None:
            return self.out_root + self.name + "/"
        
        out_paths = {}
        for subdir in self.subdirs:
            out_paths[subdir] = self.out_root + self.name + "/" + subdir + "/"
        return out_paths
# def run_downloader():
    # # Path to the downloader
    # # More info about the downloader: https://github.com/ondyari/FaceForensics/blob/master/dataset/README.md
    # DOWNLOADER_PATH = "../FaceForensics/downloader/download-FaceForensics.py"

    # # Run the downloader
    # os.system(f"python ./utils/forensics_downloader.py {DOWNLOADER_PATH}")

if __name__ == "__main__":

    # Run the downloader on a different process and wait for it to continue the extraction
    # child = Process(target=run_downloader)
    # child.start()
    # child.join()

    # ROOT_INPUT_DIR = "../VideoData"
    # ROOT_OUTPUT_DIR = "../ExtractedFaces"
    # # FORENSICS PATHS
    # TECHNIQUES = ["NeuralTextures", "FaceShifter",
    #               "Deepfakes", "Face2Face", "FaceSwap"]
    # COMPRESSION = ["c23"]
    # FORENSICS_INPUT_PATHS = [
    #     f"{ROOT_INPUT_DIR}/Forensics_pp/manipulated_sequences/{x}/{y}/videos/" for x in TECHNIQUES for y in COMPRESSION] + [f"{ROOT_INPUT_DIR}/Forensics_youtube/"]

    # FORENSICS_OUTPUT_PATHS = [
    #     f"{ROOT_OUTPUT_DIR}/Forensics_pp/{x}/" for x in TECHNIQUES] + [f"{ROOT_OUTPUT_DIR}/Forensics_youtube/"]
    
    # # CELEB-DF2 PATHS
    # CELEB = ["CelebDF", "Celeb-real", "YouTube-real"]

    # # INPUT PATHS
    # INPUT_PATHS = [f"{ROOT_INPUT_DIR}/{x}/" for x in CELEB] + FORENSICS_INPUT_PATHS
    # OUTPUT_PATHS = [f"{ROOT_OUTPUT_DIR}/{x}/" for x in CELEB] + FORENSICS_OUTPUT_PATHS
    # PARAMS = []
    # for in_path, out_path, param in zip(INPUT_PATHS, OUTPUT_PATHS, PARAMS):
    #     os.system(
    #         f"python ./utils/FaceExtractor_random_frames.py -i {in_path} -o {out_path}")
        
    # Forensics = {
    #     "subdirs": ["NeuralTextures", "FaceShifter", "Deepfakes", "Face2Face", "FaceSwap"],
    #     "num_bins": 10,
    #     "sample_size": 10
    # }
        
# os.system(f"python ./utils/FaceExtractor_random_frames.py -i {in_path} -o {out_path} -b {Forensics["num_bins"]} -s {Forensics["sample_size"]}")

    #Negative samples
    Forensics = VideoDataset("Forensicspp", "../VideoData/Forensics_pp/", "./ExtractedFaces/", 
                            subdirs = ["NeuralTextures", "FaceShifter", "Deepfakes", "Face2Face", "FaceSwap"], sample_size = 2)
    
    CelebDF = VideoDataset("CelebDF", "../VideoData/CelebDF/", "./ExtractedFaces/", sample_size=2)
    # Positvie samples
    CelebReal = VideoDataset("Celeb-real", "../VideoData/Celeb-real/","./ExtractedFaces/", sample_size=10)
    YouTubeReal = VideoDataset("YouTube-real", "../VideoData/YouTube-real/", "./ExtractedFaces/", sample_size=10)
    Forensics_youtube = VideoDataset("Forensics_youtube", "../VideoData/Forensics_youtube/", "./ExtractedFaces/", sample_size=5)
    
    datasets = [Forensics, CelebDF, CelebReal, YouTubeReal, Forensics_youtube]

    for ds in datasets:
        if type(ds.out_paths) == dict: 
            for subdir in ds.out_paths:
                # os.system(f"python ./utils/FaceExtractor_random_frames.py -i {ds.root} -o {ds.out_paths[subdir]} -b {ds.num_bins} -s {ds.sample_size}")
                print(
                    f"python ./utils/FaceExtractor_random_frames.py -i {ds.root} -o {ds.out_paths[subdir]} -b {ds.num_bins} -s {ds.sample_size}")
        else:  
            print(
                f"python ./utils/FaceExtractor_random_frames.py -i {ds.root} -o {ds.out_paths} -b {ds.num_bins} -s {ds.sample_size}")
