import argparse

program_name = "Argument Parsing"
description = "Experiment with argument parsing"
epilog = "This text is shown at the bottom of help"

parser = argparse.ArgumentParser(
    prog=program_name,
    description=description,
    epilog=epilog
)

parser.add_argument("letters", type=str, choices=["a", "b", "c"], default="a")
parser.add_argument("-n", "--number", type=int, required=True, help="This takes a number")
parser.add_argument("-s", "--str", type=str, help="This takes a string")

args = parser.parse_args()

parser.print_help()
print("\n========== ========== ========== ========== ==========\n")

print(f"args: {args}")
print(f"args.letters: {args.letters}")