import argparse

# Creating a parser object
parser = argparse.ArgumentParser(
    description="A simple command line interface.")

# Adding arguments
parser.add_argument("name", help="Your name")
parser.add_argument(
    "-n", "--number",
    help="Number of times to repeat the message",
    type=int,
    default=1
)

# Parsing arguments
args = parser.parse_args()

# Using the arguments
print("Hello, " + args.name * args.number)
