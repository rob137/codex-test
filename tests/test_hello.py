import unittest
import hello


class TestHello(unittest.TestCase):
    def test_greet_default(self):
        self.assertEqual(hello.greet(), "Hello, World!")

    def test_greet_custom(self):
        self.assertEqual(hello.greet("Alice"), "Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
