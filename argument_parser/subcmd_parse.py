import argparse

prog_name = "Subcommand Parsing"
desc = "Main Parser"
epilog = "End of help"

parser = argparse.ArgumentParser(prog=prog_name, description=desc, epilog=epilog)
sub_parser = parser.add_subparsers()

parser.add_argument("run", type=str, choices=["run"])

sub_parser.add_parser("train")
sub_parser.add_parser("test")

args = parser.parse_args()

print(args)

