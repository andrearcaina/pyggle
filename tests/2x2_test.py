import unittest
from pyggle.boggle import Boggle
from pyggle.functions import solve

# testing 2x2 boards through string or list of lists with or without words

class TestBoggle(unittest.TestCase):
    def setUp(self):
        with open('sample_data.txt', 'r') as file:
            self.words = [line.strip() for line in file]
    
    def test_not_official(self):
        board = [['e', 'a'], ['s', 't']]
        boggle = Boggle(board, self.words)
        result = solve(boggle)
        expected_result = {'a': [(0, 1)], 'as': [(0, 1), (1, 0)], 'at': [(0, 1), (1, 1)], 'east': [(0, 0), (0, 1), (1, 0), (1, 1)], 
                            'eat': [(0, 0), (0, 1), (1, 1)], 'sea': [(1, 0), (0, 0), (0, 1)], 'seat': [(1, 0), (0, 0), (0, 1), (1, 1)], 'set': [(1, 0), (0, 0), (1, 1)], 'tea': [(1, 1), (0, 0), (0, 1)]}
        self.assertEqual(result, expected_result)

    def test_yes_official(self):
        board = [['e', 'a'], ['s', 't']]
        boggle = Boggle(board, self.words, True)
        result = solve(boggle)
        expected_result = {'east': [(0, 0), (0, 1), (1, 0), (1, 1)], 'eat': [(0, 0), (0, 1), (1, 1)], 
                            'sea': [(1, 0), (0, 0), (0, 1)], 'seat': [(1, 0), (0, 0), (0, 1), (1, 1)], 
                            'set': [(1, 0), (0, 0), (1, 1)], 'tea': [(1, 1), (0, 0), (0, 1)]}
        self.assertEqual(result, expected_result)

    def test_string(self):
        board = 'ea st'
        boggle = Boggle(board, self.words)
        result = solve(boggle)
        expected_result = {'a': [(0, 1)], 'as': [(0, 1), (1, 0)], 'at': [(0, 1), (1, 1)], 'east': [(0, 0), (0, 1), (1, 0), (1, 1)], 
                            'eat': [(0, 0), (0, 1), (1, 1)], 'sea': [(1, 0), (0, 0), (0, 1)], 'seat': [(1, 0), (0, 0), (0, 1), (1, 1)], 'set': [(1, 0), (0, 0), (1, 1)], 'tea': [(1, 1), (0, 0), (0, 1)]}
        self.assertEqual(result, expected_result)

    def test_no_words(self):
        board = "ea st"
        boggle = Boggle(board)
        result = solve(boggle)
        expected_result = {'a': [(0, 1)], 'ae': [(0, 1), (0, 0)], 'aes': [(0, 1), (0, 0), (1, 0)], 
                            'aet': [(0, 1), (0, 0), (1, 1)], 'as': [(0, 1), (1, 0)], 'ase': [(0, 1), (1, 0), (0, 0)], 
                            'ast': [(0, 1), (1, 0), (1, 1)], 'at': [(0, 1), (1, 1)], 'ate': [(0, 1), (1, 1), (0, 0)], 
                            'ates': [(0, 1), (1, 1), (0, 0), (1, 0)], 'e': [(0, 0)], 'ea': [(0, 0), (0, 1)], 
                            'east': [(0, 0), (0, 1), (1, 0), (1, 1)], 'eat': [(0, 0), (0, 1), (1, 1)], 
                            'eats': [(0, 0), (0, 1), (1, 1), (1, 0)], 'es': [(0, 0), (1, 0)], 'est': [(0, 0), (1, 0), (1, 1)], 
                            'et': [(0, 0), (1, 1)], 'eta': [(0, 0), (1, 1), (0, 1)], 'etas': [(0, 0), (1, 1), (0, 1), (1, 0)], 
                            's': [(1, 0)], 'sa': [(1, 0), (0, 1)], 'sae': [(1, 0), (0, 1), (0, 0)], 
                            'sat': [(1, 0), (0, 1), (1, 1)], 'sate': [(1, 0), (0, 1), (1, 1), (0, 0)], 
                            'se': [(1, 0), (0, 0)], 'sea': [(1, 0), (0, 0), (0, 1)], 'seat': [(1, 0), (0, 0), (0, 1), (1, 1)], 
                            'set': [(1, 0), (0, 0), (1, 1)], 'seta': [(1, 0), (0, 0), (1, 1), (0, 1)], 'st': [(1, 0), (1, 1)], 
                            'sta': [(1, 0), (1, 1), (0, 1)], 't': [(1, 1)], 'ta': [(1, 1), (0, 1)], 
                            'tae': [(1, 1), (0, 1), (0, 0)], 'tas': [(1, 1), (0, 1), (1, 0)], 'te': [(1, 1), (0, 0)], 
                            'tea': [(1, 1), (0, 0), (0, 1)], 'teas': [(1, 1), (0, 0), (0, 1), (1, 0)], 'ts': [(1, 1), (1, 0)]}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
