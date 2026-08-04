import argparse

program_name = "Argument Parsing"
description = "Experiment with argument parsing"
epilog = "This text is shown at the bottom of help"

parser = argparse.ArgumentParser(
    prog=program_name,
    description=description,
    epilog=epilog
)

parser.add_argument("what")

arguments = parser.parse_args()

if (arguments == "what"):
    print("'what' was passed as argument")
else:
    print("'what' was not passed as argument")