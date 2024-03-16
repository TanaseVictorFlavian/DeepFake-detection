import os
from multiprocessing import Process
from Classes.VideoDataset import VideoDataset

"""
This script automates the face extraction from video sources.
It has a feature for the specific usecase when the user has to download 
the FaceForensics++ dataset beforehand.
"""

def run_downloader():
    # Path to the downloader
    # More info about the downloader: https://github.com/ondyari/FaceForensics/blob/master/dataset/README.md
    DOWNLOADER_PATH = "../FaceForensics/downloader/download-FaceForensics.py"

    # Run the downloader
    os.system(f"python ./utils/forensics_downloader.py {DOWNLOADER_PATH}")

if __name__ == "__main__":

    # Run the downloader on a different process and wait for it to continue the extraction
    # child = Process(target=run_downloader)
    # child.start()
    # child.join()

    # os.system(f"python ./utils/FaceExtractor_random_frames.py -i {in_path} -o {out_path} -b {Forensics["num_bins"]} -s {Forensics["sample_size"]}")

    #Negative samples

    IN_ROOT = "../VideoData/"
    OUT_ROOT = "../ExtractedFaces/"  

    Forensics = VideoDataset("Forensicspp", f"{IN_ROOT}Forensics_pp/", OUT_ROOT, 
                            subdirs = ["NeuralTextures", "FaceShifter", "Deepfakes", "Face2Face", "FaceSwap"], sample_size = 2)
    
    CelebDF = VideoDataset("CelebDF", f"{IN_ROOT}CelebDF/", OUT_ROOT, sample_size=2)
    # Positvie samples
    CelebReal = VideoDataset("Celeb-real", f"{IN_ROOT}Celeb-real/",OUT_ROOT, sample_size=10)
    YouTubeReal = VideoDataset("YouTube-real", f"{IN_ROOT}YouTube-real/", OUT_ROOT, sample_size=10)
    Forensics_youtube = VideoDataset("Forensics_youtube", f"{IN_ROOT}Forensics_youtube/", OUT_ROOT, sample_size=5)
    
    datasets = [Forensics, CelebDF, CelebReal, YouTubeReal, Forensics_youtube]

    for ds in datasets:
        if ds.subdirs is not None:
            for subdir in ds.out_paths:
                # os.system(f"python ./utils/extract_frames.py -i {ds.root} -o {ds.out_paths[subdir]} -b {ds.num_bins} -s {ds.sample_size}")
                os.system(
                    f"python ./utils/extract_frames.py -i {ds.in_paths[subdir]} -o {ds.out_paths[subdir]} -b {ds.num_bins} -s {ds.sample_size}")
        else:  
            os.system(
                f"python ./utils/extract_frames.py -i {ds.in_root} -o {ds.out_paths} -b {ds.num_bins} -s {ds.sample_size}")
        # os.system("python ./utils/extract_frames.py -i ../VideoData/Forensics_pp//NeuralTextures/ -o ../ExtractedFaces/Forensicspp/NeuralTextures/ -b 20 -s 2")
