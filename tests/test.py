import unittest
from utils import limit_chars as lc


class MyTestCase(unittest.TestCase):
    def test_limit_chars(self):
        self.assertEqual(lc.limit_chars("Hello this is a test", 10, True), "Hello t...")  # add assertion here
        self.assertEqual(lc.limit_chars("This is my test case for the function", 20, False, ), "This is my test case")
        self.assertEqual(lc.limit_chars("This is my test case for the function", 13, True, "   "), "This is my   ")
        with self.assertRaises(lc.LimitBiggerThanString):
            lc.limit_chars("Hello world", 12, True, replace_whitespace=False)


if __name__ == '__main__':
    unittest.main()
