from torchvision import models, transforms
from torch.utils.data import DataLoader
from helpers.CustomDataset import CustomDataset
import torch.nn as nn
import torch


def get_model(model_name,
                     test_data_path,
                     test_csv_path,
                     ):
    if model_name == "effnet_b0_pretrained":
        # Define transforms for effnet_b0

        test_transforms = transforms.Compose([
            transforms.Resize(
                (256, 256), interpolation=transforms.InterpolationMode.BICUBIC),
            transforms.CenterCrop((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225]),
        ])
        # Define the test dataset
        test_dataset = CustomDataset(
            test_csv_path, test_data_path, test_transforms)

        # Define test loader
        test_loader = DataLoader(dataset=test_dataset,
                                 batch_size=64,
                                 shuffle=True)

        model = models.efficientnet_b0(
            weights=models.EfficientNet_B0_Weights.DEFAULT)

        model.classifier = nn.Sequential(
            nn.Dropout(p=0.4, inplace=True),
            nn.Linear(1280, 2),
        )

        state_dict = torch.load(
            'models/model_weights/effnet_b0_pretrained.pth')

        model.load_state_dict(state_dict)

        return model, test_loader
