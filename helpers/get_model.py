from torchvision import models
from torchvision.models import efficientnet_b0, EfficientNet_B0_Weights
from torchvision import transforms
import torch.nn as nn
import torch


def get_model(model_name):
    # Returns the model ready to be evaluated
    # and the transforms needed for passing data through the model
    if model_name == "effnet_b0_pretrained":
        # Define transforms for effnet_b0

        img_transforms = transforms.Compose([
            transforms.Resize(
                (256, 256), interpolation=transforms.InterpolationMode.BICUBIC),
            transforms.CenterCrop((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225]),
        ])

        model = models.efficientnet_b0(
            weights=models.EfficientNet_B0_Weights.DEFAULT)

        model.classifier = nn.Sequential(
            nn.Dropout(p=0.4, inplace=True),
            nn.Linear(1280, 2),
        )

        model_path = 'models/model_weights/effnet_b0_pretrained.pth'
        model.load_state_dict(torch.load(model_path,
                                         map_location=torch.device('cpu')))

        return model, img_transforms
