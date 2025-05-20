"""A bog-standard greeting module."""

def greet(name="World"):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


import argparse


def main(argv=None):
    """Print a greeting to stdout."""
    parser = argparse.ArgumentParser(description="Print a greeting")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args(argv)
    print(greet(args.name))


if __name__ == "__main__":
    main()
