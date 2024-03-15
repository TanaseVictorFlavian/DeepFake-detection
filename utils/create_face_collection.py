import os
from multiprocessing import Process
"""
This script automates the face extraction from video sources.
It has a feature for the specific usecase when the user has to download 
the FaceForensics++ dataset beforehand.
"""

def run_downloader():
    # Path to the downloader
    # More info about the downloader: https://github.com/ondyari/FaceForensics/blob/master/dataset/README.md
    DOWNLOADER_PATH = "../FaceForensics/downloader/downloader.py"

    # Run the downloader
    os.system(f"python ./utils/Forensics_downloader.py {DOWNLOADER_PATH}")

if __name__ == "__main__":

    # Run the downloader on a different process and wait for it to continue the extraction
    child = Process(target=run_downloader)
    child.start()
    child.join()

    ROOT_INPUT_DIR = "../VideoData"
    ROOT_OUTPUT_DIR = "../ExtractedFaces"
    # FORENSICS PATHS
    TECHNIQUES = ["NeuralTextures", "FaceShifter",
                  "Deepfakes", "Face2Face", "FaceSwap"]
    COMPRESSION = ["c23"]
    FORENSICS_INPUT_PATHS = [
        f"{ROOT_INPUT_DIR}/Forensics_pp/manipulated_sequences/{x}/{y}/videos/" for x in TECHNIQUES for y in COMPRESSION]

    FORENSICS_OUTPUT_PATHS = [
        f"{ROOT_OUTPUT_DIR}/Forensics_pp/{x}/" for x in TECHNIQUES]
    
    # CELEB-DF2 PATHS
    CELEB = ["CelebDF", "Celeb-real", "YouTube-real"]

    # INOUT PATHS
    INPUT_PATHS = [f"{ROOT_INPUT_DIR}/{x}/" for x in CELEB] + FORENSICS_INPUT_PATHS
    OUTPUT_PATHS = [f"{ROOT_OUTPUT_DIR}/{x}/" for x in CELEB] + FORENSICS_OUTPUT_PATHS

    for in_path, out_path in zip(INPUT_PATHS, OUTPUT_PATHS):
        os.system(
            f"python ./utils/FaceExtractor.py -i {in_path} -o {out_path}")
