from typing import Any

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import v2

# Batch Size
BS = 64
# Width, Height of image
W, H = 28, 28
# Hidden Layer Size
HIDDEN = 512
# Number of Output Class
CLS = 10

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]),
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]),
)


train_dataloader = DataLoader(training_data, batch_size=BS)
test_dataloader = DataLoader(test_data, batch_size=BS)

for X, y in test_dataloader:
    print(f"Shape of X [BS, Channel, Height, Weight]: {X.shape}")
    H = X.shape[2]
    W = X.shape[3]
    print(f"Shape of y: {y.shape} {y.dtype}")
    break

# accelerator = torch.accelerator.current_accelerator()
# device = accelerator.type if accelerator is not None else "cpu"
device = torch.device("cpu")
print(f"Using {device} device")


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(H * W, HIDDEN),
            nn.ReLU(),
            nn.Linear(HIDDEN, HIDDEN),
            nn.ReLU(),
            nn.Linear(HIDDEN, CLS),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


model = NeuralNetwork().to(device=device)
print(model)

# TODO:
# https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
