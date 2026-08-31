import torch
import string
import unicodedata

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
