__author__ = 'jarethmoyo'

import unittest
import Main.PMi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Main.PMi.length_of_list([]), 0)


if __name__ == '__main__':
    unittest.main()
