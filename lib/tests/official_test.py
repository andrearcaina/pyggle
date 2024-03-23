import unittest
from pyggle.boggle import Boggle
from pyggle.functions import solve

# this is testing when total board length < official length (which is 3)

class TestBoggle(unittest.TestCase):
    def setUp(self):
        with open('sample_data.txt', 'r') as file:
            self.words = [line.strip() for line in file]
    
    def test_lists(self):
        board = [['e'], ['s']]
        boggle = Boggle(board, self.words, True)
        result = solve(boggle)
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_string(self):
        board = "e s"
        boggle = Boggle(board, self.words, True)
        result = solve(boggle)
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_no_words(self):
        board = "e s"
        boggle = Boggle(board, None, True)
        result = solve(boggle)
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_random(self):
        board = "eee"
        boggle = Boggle(board, self.words, True)
        result = solve(boggle)
        expected_result = {}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
