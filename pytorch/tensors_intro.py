import torch

if torch.accelerator.is_available():
    device = torch.accelerator.current_accelerator()
    torch.set_default_device(device)

size = 2000
print_flag = False

x = torch.linspace(-torch.pi, torch.pi, size)
y = torch.sin(x)

if print_flag:
    print(f"x: {x}")
    print(f"y: {y}")

a = torch.randn(())
b = torch.randn(())
c = torch.randn(())
d = torch.randn(())

learning_rate = 1e-6

for t in range(size):
    y_pred = a + (b * x) + (c * x ** 2) + (d * x ** 3)
    
    if print_flag:
        print(f"y_pred: {y_pred}")




# data = [[1,4,2], [5,3,1]]
# tensor = torch.tensor(data)
# print(tensor)

# shape = (2, 3)

# ones = torch.ones(shape, dtype=torch.float)
# zeros = torch.zeros(shape, dtype=torch.float)
# rand = torch.rand(shape)

# print(ones)
# print(zeros)
# print(rand)

# print(f"tensor shape: {tensor.shape}")
# print(f"tensor datatype: {tensor.dtype}")
# print(f"tensor device: {tensor.device}")

# device = torch.accelerator.current_accelerator() if torch.accelerator.is_available() else "cpu"
# tensor = tensor.to(device)

# print(f"tensor device now: {tensor.device}")
# print(f"ones device: {ones.device}")