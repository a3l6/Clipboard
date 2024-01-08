import unittest
import utils.limit_chars as lc


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(lc.limit_chars("Hello this is a test", 10, True), "Hello t...")  # add assertion here

    def test_2(self):
        self.assertEqual(lc.limit_chars("This is my test case for the function", 20, False, ), "This is my test case")

    def test_3(self):
        self.assertEqual(lc.limit_chars("This is my test case for the function", 13, True, "   "), "This is my   ")

    def test_4(self):
        with self.assertRaises(lc.LimitBiggerThanString):
            lc.limit_chars("Hello world", 12, True, replace_whitespace=False)


if __name__ == '__main__':
    unittest.main()
