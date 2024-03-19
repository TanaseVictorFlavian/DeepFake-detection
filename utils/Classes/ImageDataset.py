import os

class ImageDataset: 
    def __init__(self, path, label, img_seq_length = None):
        self.path = path
        self.img_seq_length = img_seq_length
        self.label = label
        self.num_samples = len(os.listdir(path))
    
            