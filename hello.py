"""A bog-standard greeting module."""

def greet(name="World"):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main():
    """Print a greeting to stdout."""
    print(greet())


if __name__ == "__main__":
    main()
