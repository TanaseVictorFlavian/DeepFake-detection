from typing import List
import torch
from torchvision import transforms
from utils.Classes.FrameExtractor import FrameExtractor
import os
from PIL import Image
# from cv2 import

def prepare_video(path, transforms) -> List[torch.tensor]:
    """
    returns a list of sampled images transformed to tensors
    """
    output_path = "path/extracted_faces/"
    frame_extractor = FrameExtractor(path, output_path)
    frame_extractor.extract_frames(num_bins=5, sample_size=3)

    image_tensors = []

    for img in os.listdir(output_path):
        image = Image.open(os.join(output_path, img))
        image = transforms(image)
        image_tensors.append(image)

    return image_tensors

def prepare_image(path, transforms) -> torch.tensor:
    """
    returns a single image transformed to tensor 
    ready to be passed through the model
    """
    image = Image.open(path)

    return [transforms(image).unsqueeze(0)]