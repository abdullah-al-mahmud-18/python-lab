import argparse

prog_name = "Subcommand Parsing"
desc = "Main Parser"
epilog = "End of help"
DIV = "==========" * 10

parser = argparse.ArgumentParser(prog=prog_name, description=desc, epilog=epilog)
parser.add_argument("run", type=str, choices=["run"])

sub_parser = parser.add_subparsers(title="Sub Parser", dest="sub")



train_parser = sub_parser.add_parser("train")
train_parser.add_argument("-t", "--type", type=str, choices=["half", "full"])


args = parser.parse_args(["run", "train", "-t", "half"])

print(args)
print(args.run)
print(args.sub)

print(f"\n{DIV}\n")
parser.print_help()
train_parser.print_help()
print(f"\n{DIV}\n")



