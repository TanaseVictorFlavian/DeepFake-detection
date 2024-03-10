import os
import subprocess
import argparse


def download_videos(downloader_path, log = False):
    
    OUTPUT_PATH = "./Videos"
    DATASETS = ["NeuralTextures", "FaceShifter",
            "Deepfakes", "Face2Face", "FaceSwap"]
    COMPRESSION = ["raw", "c23", "c40"]
    NUM_SAMPLES = [1, 1, 1]
    SERVER = "EU2"

    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH, exist_ok=True)

    for dataset in DATASETS:
        for i in range(3):
            cmd = f"python {downloader_path} {OUTPUT_PATH} -d {dataset} -c {COMPRESSION[i]} -n {NUM_SAMPLES[i]} --server {SERVER}"
            if log:
                print(cmd)

            process = subprocess.Popen(
                cmd, stdin=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == 'nt' else 0)
            process.stdin.write("\n")
            process.stdin.flush()
            process.wait()
            process.stdin.close()
    print("Done")   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Automated download of the FaceForensics++ dataset',
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