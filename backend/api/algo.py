from pyggle import Boggle

board = [['e', 'a'], ['s', 't']]
    
with open('data/word_list_3000.txt', 'r') as file:
    words = [line.strip() for line in file]

boggle = Boggle(board, words)

boggle.print_result()