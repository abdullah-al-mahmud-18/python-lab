from typing import Any

import torch
import string
import unicodedata

from io import open
import os
import time
import glob

from torch.utils.data import Dataset

PRINT = True

device = torch.device("cpu")

if torch.cuda.is_available():
    device = torch.device("cuda")

torch.set_default_device(device)
if PRINT:
    print(f"current device: {torch.get_default_device()}")

# We can use "_" to represent an out-of-vocabulary character, that is, any character we are not handling in our model
allowed_characters = string.ascii_letters + " .,;'" + "_"
n_letters = len(allowed_characters)

def unicode_to_ascii(s):
    list = []
    for c in unicodedata.normalize('NFD', s):
        if unicodedata.category(c) != 'Mn' and c in allowed_characters:
            list.append(c)
    return "".join(list)

def letter_to_index(letter):
    if letter not in allowed_characters:
        return allowed_characters.find("_")
    return allowed_characters.find(letter)

def line_to_tensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letter_to_index(letter)] = 1
    return tensor

if PRINT:
    print(f"converting 'Ślusàrski' to {unicode_to_ascii('Ślusàrski')}")
    print(f"letter c to index: {letter_to_index("c")}")
    print (f"The letter 'a' becomes {line_to_tensor('a')}") #notice that the first position in the tensor = 1
    print (f"The name 'Ahn' becomes {line_to_tensor('Ahn')}") #notice 'A' sets the 27th index to 1


class NamesDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.load_time = time.localtime
        labels_set = set()

        self.data = []
        self.data_tensors = []
        self.labels = []
        self.labels_tensors = []

        text_files = glob.glob(os.path.join(data_dir, "*.txt"))
        for file_name in text_files:
            label = os.path.splitext(os.path.basename(file_name))[0]
            labels_set.add(label)
            lines = open(file_name, encoding='utf-8').read().strip().split('\n')

            for name in lines:
                self.data.append(name)
                self.data_tensors.append(line_to_tensor(name))
                self.labels.append(label)

    def __len__(self):
        pass

    def __getitem__(self):
        pass