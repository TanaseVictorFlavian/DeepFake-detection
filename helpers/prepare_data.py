from typing import List
import torch
from torchvision import transforms
from utils.Classes.FrameExtractor import FrameExtractor
import os
from PIL import Image
from torchvision.transforms import transforms
from helpers.print_image_from_tensor import print_image_from_tensor

# from cv2 import

def prepare_video(path, transforms, tta_enabled) -> List[torch.tensor]:
    """
    returns a list of sampled images transformed to tensors
    """
    output_path = "./uploads/frames"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    frame_extractor = FrameExtractor(path, output_path)
    frame_extractor.extract_faces(num_bins=5, sample_size=3)

    image_tensors = []

    for img in os.listdir(output_path):
        image = Image.open(os.path.join(output_path, img))
        image = transforms(image).unsqueeze(0)
        image_tensors.append(image)

    return image_tensors


def prepare_image(path, img_transforms, tta_enabled) -> torch.tensor:
    """
    returns a single image transformed to tensor 
    ready to be passed through the model
    """
    image = Image.open(path)
    if tta_enabled:
        print("TTA ENABLED")
        aug_images = tta([image], img_transforms)
        # Uncomment this code do save and show augumented images

        # for i, img in enumerate(aug_images):
        #     t_image = print_image_from_tensor(img)
        #     t_image.save(f"transforms_samples/aug_{i}.png")

        return aug_images 
    else:
        return [img_transforms(image).unsqueeze(0)]

def tta(data, img_transforms) -> list:
    AUGUMENTATIONS = [
        transforms.RandomHorizontalFlip(p=1.0), 
        transforms.RandomVerticalFlip(p=1.0),
        transforms.ColorJitter(
            brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
        transforms.RandomEqualize(p=1.0),
        transforms.RandomSolarize(p=1.0, threshold=156),
        ]  
    # Apply augumentation for image 
    if len(data) == 1: 
        image = data.pop()
        aug_images = []
        for t in AUGUMENTATIONS:    
            complete_transform  = lambda x : img_transforms(t(x))
            aug_images.append(complete_transform(image).unsqueeze(0))

        return aug_images