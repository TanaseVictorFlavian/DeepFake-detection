import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torchvision
from torchvision import datasets, models, transforms
from torchvision.models import resnet50
from helpers import evaluation, plotting, training

# PARAMS

BATCH_SIZE = 64
NUM_EPOCHS = 100
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
RANDOM_SEED = 2002

print(f"Device = {DEVICE}")

# TRANSFORMS

train_transforms = torchvision.transforms.Compose([
    torchvision.transforms.Resize((256, 256)),
    torchvision.transforms.RandomCrop((224, 224)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize( mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
])

test_transforms = torchvision.transforms.Compose([
    torchvision.transforms.Resize((70, 70)),
    torchvision.transforms.CenterCrop((64, 64)),
    torchvision.transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
