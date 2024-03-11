import os
import subprocess
import argparse


"""
@inproceedings{roessler2019faceforensicspp,
	author = {Andreas R\"ossler and Davide Cozzolino and Luisa Verdoliva and Christian Riess and Justus Thies and Matthias Nie{\ss}ner},
	title = {Face{F}orensics++: Learning to Detect Manipulated Facial Images},
	booktitle= {International Conference on Computer Vision (ICCV)},
	year = {2019}
}

This simple function automates the usage of the FaceForensics++ dataset downloader.
More info about the downlaoder: https://github.com/ondyari/FaceForensics/blob/master/dataset/README.md
Modifiy the parameters for your own needs.
"""
def download_videos(downloader_path, log = False):
    
    OUTPUT_PATH = "../VideoData/Forensics_pp"
    DATASETS = ["NeuralTextures", "FaceShifter",
            "Deepfakes", "Face2Face", "FaceSwap"]
    
    # Each compression level is mapped to a number of samples
    COMPRESSION = ["c23"]
    NUM_SAMPLES = [5]
    SERVER = "EU2"

    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH, exist_ok=True)

    if len(COMPRESSION) != len(NUM_SAMPLES):
        print("Invalid parameter combination")
        return

    for dataset in DATASETS:
        for i in range(len(COMPRESSION)):
            cmd = f"python {downloader_path} {OUTPUT_PATH} -d {dataset} -c {COMPRESSION[i]} -n {NUM_SAMPLES[i]} --server {SERVER}"
            if log:
                print(cmd)

            process = subprocess.Popen(
                cmd, stdin=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == 'nt' else 0)
            process.stdin.write("\n")
            process.stdin.flush()
            process.wait()
            process.stdin.close()
    print(f"\033[33mDownload Completed at : {OUTPUT_PATH}\033[0m")


if __name__ == "__main__":
    # Example of CLI input : python ./Forensics_downloader.py ../FaceForensics/downloader/downloader.py --log
    
    parser = argparse.ArgumentParser(
        description='Automated downloader of the FaceForensics++ dataset',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('downloader_path', type=str,
                        help='Path to the downloader.py script')
    
    parser.add_argument('--log', action='store_true', help='Show the commands ran by the script')
    
    args = parser.parse_args()

    if not os.path.exists(args.downloader_path):
        error_message = f"\033[91mPath {args.downloader_path} is invalid'\033[0m'"
        raise FileNotFoundError(error_message)
    
    if args.log:
        download_videos(args.downloader_path, log = True)
    else:
        download_videos(args.downloader_path)

