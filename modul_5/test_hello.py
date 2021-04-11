import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello_python(self):
        self.assertEqual(hello.hello_python(), "Hello Python!")

    def test_hello_name(self):
        self.assertEqual(hello.hello_name(), "Hello Ghita!")
        self.assertEqual(hello.hello_name("Marian"), "Hello Marian!")
        self.assertRaises(ValueError, hello.hello_name, "M")
        with self.assertRaises(ValueError):
            hello.hello_name("M")


if __name__ == "__main__":
    unittest.main()
