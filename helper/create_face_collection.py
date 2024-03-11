import os
import argparse


"""
This script automates the face extraction from video sources.
It has a feature for the specific usecase when the user has to download 
the FaceForensics++ dataset beforehand.
"""

if __name__ == "__main__":
    pid = os.fork()

    if pid == 0:
        # Path to the downloader
        # More info about the downlaoder: https://github.com/ondyari/FaceForensics/blob/master/dataset/README.md
        DOWNLOADER_PATH = "../FaceForensics/downloader/downloader.py"

        # Run the downloader
        os.system(f"python Forensics_downloader.py {DOWNLOADER_PATH}")
        os._exit(0)

    else:
        # Wait for the download to finish
        os.waitpid(pid, 0)
    # ../VideoData/Forensics_pp/manipulated_sequences/Deepfakes/c23/videos
    TECHNIQUES = ["NeuralTextures", "FaceShifter", "Deepfakes", "Face2Face", "FaceSwap"]
    FORENSICS_PATHS = [
        f"../VideoData/Forensics_pp/manipulated_sequences/{x}/c23/videos/" for x in TECHNIQUES]
    VIDEO_PATHS = ["../VideoData/CelebDF/"] + FORENSICS_PATHS
    OUTPUT_PATH = "./data/Negative_images/"

    for vp in VIDEO_PATHS:
        os.system(
            f"python FaceExtractor.py -i {vp} -o {OUTPUT_PATH} -sf 1 -ef 100")