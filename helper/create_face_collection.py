import os
import argparse


"""
This script automates the face extraction from video sources.
It has a feature for the specific usecase when the user has to download 
the FaceForensics++ dataset beforehand.
"""

if __name__ == "__main__":
    

    # pid = os.fork()

    # if pid == 0:
    #     # Path to the downloader
    #     # More info about the downlaoder: https://github.com/ondyari/FaceForensics/blob/master/dataset/README.md
    #     DOWNLOADER_PATH = "../FaceForensics/downloader/downloader.py"

    #     # Run the downloader
    #     os.system(f"python Forensics_downloader.py {DOWNLOADER_PATH}")
    #     os._exit(0)

    # else:
    #     # Wait for the download to finish
    #     os.waitpid(pid, 0)
    # ../VideoData/Forensics_pp/manipulated_sequences/Deepfakes/c23/videos
    TECHNIQUES = ["NeuralTextures", "FaceShifter", "Deepfakes", "Face2Face", "FaceSwap"]
    COMPRESSION = ["c23"]
    FORENSICS_INPUT_PATHS = [
        f"../VideoData/Forensics_pp/manipulated_sequences/{x}/{y}/videos/" for x in TECHNIQUES for y in COMPRESSION]
    INPUT_PATHS = ["../VideoData/CelebDF/"] + FORENSICS_INPUT_PATHS
    FORENSICS_OUTPUT_PATHS = [f"../ExtractedFaces/Forensics_pp/{x}/" for x in TECHNIQUES]
    OUTPUT_PATHS = ["../ExtractedFaces/CelebDF/"] + FORENSICS_OUTPUT_PATHS
    #TODO create other paths from a root path

    for in_path, out_path in zip(FORENSICS_INPUT_PATHS, FORENSICS_OUTPUT_PATHS):
        os.system(
            f"python ./helper/FaceExtractor.py -i {in_path} -o {out_path}")   
        # print(f"python FaceExtractor.py -i {in_path} -o {out_path}")

    # for x in INPUT_PATHS:
    #     print(x)

    # for x in OUTPUT_PATHS:
    #     print(x)