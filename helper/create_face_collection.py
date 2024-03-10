import os
"""
@inproceedings{roessler2019faceforensicspp,
	author = {Andreas R\"ossler and Davide Cozzolino and Luisa Verdoliva and Christian Riess and Justus Thies and Matthias Nie{\ss}ner},
	title = {Face{F}orensics++: Learning to Detect Manipulated Facial Images},
	booktitle= {International Conference on Computer Vision (ICCV)},
	year = {2019}
}
"""

if __name__ == "__main__":
    pid = os.fork()
    


    if pid == 0:
        # Child process

        # Path to the downloader
        # More info : https://github.com/ondyari/FaceForensics/tree/master
        DOWNLOADER_PATH = "../FaceForensics/downloader/downloader.py"
        
        # Run the downloader
        os.system(f"python Forensics_downloader.py {DOWNLOADER_PATH}")
        os._exit(0)
    
    else:
        # Wait for the download to conclude
        os.waitpid(pid, 0) 

    # Create the face collection from the data downloaded at ./Videos
    VIDEO_PATH = "./Videos"
    OUTPUT_PATH = "./face_collection"
    

