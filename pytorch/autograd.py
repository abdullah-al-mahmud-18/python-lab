import torch
from torch.nn.functional import binary_cross_entropy_with_logits

# Input tensors
x = torch.ones(5)

# Output 
y = torch.zeros(3)

# Weights w and Bias b
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3)
b.requires_grad_(True) # another way of enabling autograd. 

z = torch.matmul(x, w) + b
loss = binary_cross_entropy_with_logits(z, y)

# TODO
# https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html

