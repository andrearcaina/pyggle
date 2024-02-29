from pyggle import Boggle 

if __name__ == "__main__":
    board = "ea st"
    # board can be [["e", "a"], ["s", "t"]] or "ea st"
    
    # this is only 3000 words, but the web demo will utilize all 479k words
    with open('data/word_list_3000.txt', 'r') as file:
        words = [line.strip() for line in file]
    
    # the second adn third argument are optional
    # if words is not given, will default to 479k word list
    # if official is not given, will default to False (will return all words, regardless of length)
    # official means "official rules of Boggle game"
    boggle = Boggle(board, words, True)

    # print full dictionary
    print(boggle.solver())
    
    # print only words
    print(boggle.get_words())

    # print only coords
    print(boggle.get_coords())

    # print score of each word
    print(boggle.get_score())

    # print word: coord format
    boggle.print_result()