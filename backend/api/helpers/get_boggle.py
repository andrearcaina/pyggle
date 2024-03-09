from pyggle import Boggle

def determine_words(given_list):
    result_words = []

    if not given_list:
        with open('data/words/words_alpha.txt', 'r') as file:
            result_words = [line.strip() for line in file]

    elif given_list == "3000":
        with open('data/words/word_list_3000.txt', 'r') as file:
            result_words = [line.strip() for line in file]

    elif given_list == "scrabble":
        with open('data/words/word_list_scrabble_2019.txt', 'r') as file:
            result_words = [line.strip() for line in file]

    return result_words

def found_words(board, word_string, official):
    boggle = Boggle(board, determine_words(word_string), official)
    return boggle.get_words()

def coordinates(board, word_string, official):
    boggle = Boggle(board, determine_words(word_string), official)
    return boggle.get_coords()

def scores(board, word_string, official):
    boggle = Boggle(board, determine_words(word_string), official)
    return boggle.get_score()
