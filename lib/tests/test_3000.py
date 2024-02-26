import unittest
from pyggle.boggle import Boggle

class TestBoggle(unittest.TestCase):
    def setUp(self):
        with open('sample_data.txt', 'r') as file:
            self.words = [line.strip() for line in file]
    
    def test_solver(self):
        board = [['e', 'a'], ['s', 't']]
        boggle = Boggle(board, self.words)
        result = boggle.solver()
        expected_result = {'a': [(0, 1)], 'as': [(0, 1), (1, 0)], 'at': [(0, 1), (1, 1)], 'east': [(0, 0), (0, 1), (1, 0), (1, 1)], 
                            'eat': [(0, 0), (0, 1), (1, 1)], 'sea': [(1, 0), (0, 0), (0, 1)], 'seat': [(1, 0), (0, 0), (0, 1), (1, 1)], 'set': [(1, 0), (0, 0), (1, 1)], 'tea': [(1, 1), (0, 0), (0, 1)]}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()