import argparse

program_name = "Argument Parsing"
description = "Experiment with argument parsing"
epilog = "This text is shown at the bottom of help"

parser = argparse.ArgumentParser(
    prog=program_name,
    description=description,
    epilog=epilog
)

parser.add_argument("person", type=str, default="person", choices=["person"])
parser.add_argument("-n", "--name", type=str, required=True, help="provide name of person")
parser.add_argument("-a", "--age", type=int, help="provide age of person")
parser.add_argument("-p", "--prof", type=str, help="provide profession of person")

args = parser.parse_args()

if args.person:
    print("Person Details:")
    print(f"Name: {args.name}")
    if args.age:
            print(f"Age: {args.age}")
    if args.prof:
        print(f"Profession: {args.prof}")
else:
    parser.print_help()