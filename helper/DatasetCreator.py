from Forensics_downloader import download_videos

class DatasetCreator:
    def __init__(self, data, target):
        self.data = data
        self.target = target
    
    def fetch_data(self):
        return 