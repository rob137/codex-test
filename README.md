# Bog-Standard Project

This repository contains a simple Python module that prints a greeting. The
`hello.py` module provides a `greet` function and can be executed directly to
print `Hello, World!`.

## Installation

Install the project in editable mode with pip:

```bash
pip install -e .
```

## Running

```
python hello.py
```

You can optionally provide a name:

```
python hello.py --name Alice
```

## Testing

The project uses the built-in `unittest` module. To run the tests:

```
python -m unittest discover -s tests
```

## License

This project is licensed under the [MIT License](LICENSE).
