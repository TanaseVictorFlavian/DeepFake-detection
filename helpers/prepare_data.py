from typing import List
import torch
from torchvision import transforms
from utils.Classes.FrameExtractor import FrameExtractor
import os
from PIL import Image
from torchvision.transforms import transforms
from helpers.print_image_from_tensor import print_image_from_tensor
from utils.Classes.SequenceExtractor import SequenceExtractor

# from cv2 import

def prepare_video(path, img_transforms, tta_enabled) -> List[torch.tensor]:
    """
    returns a list of sampled images transformed to tensors
    """

    image_tensors = []
    output_path = "./uploads/frames/"
    if tta_enabled:
        print("TTA ENABLED")
        # Get a list of frames at the beginning of the video
        seq_extractor = SequenceExtractor(path, output_path)
        sampled_frames = seq_extractor.extract_faces()

        # keep only half of the frames 
    
        sampled_frames = [Image.fromarray(f) for i,f in enumerate(sampled_frames) if i % 2 == 0]
        image_tensors = tta(sampled_frames, img_transforms)

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    frame_extractor = FrameExtractor(path, output_path)
    random_samples = frame_extractor.extract_faces(num_bins=5, sample_size=3)
    
    for s in random_samples:
        image_tensors.append(img_transforms(Image.fromarray(s)).unsqueeze(0))

    return image_tensors


def prepare_image(path, img_transforms):
    """
    returns a single image transformed to tensor 
    ready to be passed through the model
    """
    image = Image.open(path)
    return [img_transforms(image).unsqueeze(0)]

def tta(data, img_transforms) -> list:
    t = transforms.RandomHorizontalFlip(p=0.5)
    aug_images = []
    
    complete_transform  = lambda x : img_transforms(t(x))
    print(type(complete_transform))
    print(type(t))
    for image in data:
        aug_images.append(complete_transform(image).unsqueeze(0))

    return aug_images