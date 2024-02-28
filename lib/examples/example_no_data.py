from pyggle import Boggle 

if __name__ == "__main__":
    board = [['e', 'a'], ['s', 't']]
    
    # given no words, will use 479k word list instead
    boggle = Boggle(board)

    # print full dictionary
    print(boggle.solver())
    
    # print only words
    print(boggle.get_words())

    # print only coords
    print(boggle.get_coords())

    # print word: coord format
    boggle.print_result()

