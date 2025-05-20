import unittest
from unittest.mock import patch
import hello


class TestHello(unittest.TestCase):
    def test_greet_default(self):
        self.assertEqual(hello.greet(), "Hello, World!")

    def test_greet_custom(self):
        self.assertEqual(hello.greet("Alice"), "Hello, Alice!")

    def test_main_default(self):
        with patch('sys.argv', ['hello.py']), patch('builtins.print') as mock_print:
            hello.main()
            mock_print.assert_called_once_with("Hello, World!")

    def test_main_custom(self):
        with patch('sys.argv', ['hello.py', '--name', 'Bob']), patch('builtins.print') as mock_print:
            hello.main()
            mock_print.assert_called_once_with("Hello, Bob!")


if __name__ == "__main__":
    unittest.main()
