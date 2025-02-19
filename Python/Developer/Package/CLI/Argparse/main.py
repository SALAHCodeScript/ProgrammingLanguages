import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser(description="A simple argument parser example.")

# Define an argument
parser.add_argument("name", type=str, help="Your name")

# Positional argument
parser.add_argument("age", type=int, help="Your age")

# Optional argument
parser.add_argument("-c", "--city", type=str, help="Your city", default="Unknown")

# Boolean flag (store_true means it's True if present, False if not)
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")

# Accept multiple values
parser.add_argument("-n", "--numbers", type=int, nargs="+", help="List of numbers")

args = parser.parse_args()

if args.verbose:
    print("Verbose mode is enabled.")
else:
    print("Verbose mode is disabled.")

# Print the argument
print(f"Hello, {args.name}!")
print(f"You are {args.age} years old and live in {args.city}.")
print(f"Numbers: {args.numbers}")
