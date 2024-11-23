
import group
import unittest

class TestCases(unittest.TestCase):

    def test_groups_of_3one(self):
        arr = [3,4,5,6,3,5,4,7,7]
        input = group.groups_of_3(arr)
        expected = [[3,4,5],[6,3,5],[4,7,7]]
        self.assertEqual(input,expected)

    def test_groups_of_3two(self):
        arr = [3,4,5,6,3,5,4,7,7,8,8]
        input = group.groups_of_3(arr)
        expected = [[3,4,5],[6,3,5],[4,7,7],[8,8]]
        self.assertEqual(input,expected)



