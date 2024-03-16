import os
from name_creator import name_creator
import shutil

if __name__ == "__main__":
    ROOT_DIR = "../FaceForensics/downloader/Videos/downloaded_videos/downloaded_videos/"
    OUTPUT_DIR = "../VideoData/Forensics_youtube/"

    for i, file in enumerate(os.listdir(ROOT_DIR)):
        video_path = ROOT_DIR + file + "/" + file + ".mp4"
        shutil.copy2(video_path, OUTPUT_DIR +
                     name_creator(i + 1, 1000) + ".mp4")
