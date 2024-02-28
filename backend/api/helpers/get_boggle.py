from pyggle import Boggle

def check(words):
    if not words:
        with open('data/words/words_alpha.txt', 'r') as file:
            words = [line.strip() for line in file]

    elif words == "3000":
        with open('data/words/word_list_3000.txt', 'r') as file:
            words = [line.strip() for line in file]

    elif words == "scrabble":
        with open('data/words/word_list_scrabble_2019.txt', 'r') as file:
            words = [line.strip() for line in file]

    return words

def bogglefy(board):
    return [list(row) for row in board.split()]

def possibilities(board, function, given_words=None):
    boggle = Boggle(bogglefy(board), check(given_words))

    if function:
        return boggle.get_words()
    
    return boggle.get_coords()