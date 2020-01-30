import os
import site
dir = os.path.dirname(os.path.dirname(__file__))
site.addsitedir(dir)

from mypkg.module import add
import unittest

class TestAdd(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_add(self):
        expected = 10
        actual = add(9, 1)
        self.assertEqual(expected, actual)


