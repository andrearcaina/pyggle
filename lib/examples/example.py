from pyggle import Boggle 

if __name__ == "__main__":
    board = [['e', 'a'], ['s', 't']]
    
    # this is only 3000 words, but the web demo will utilize 380k words
    with open('sample_data.txt', 'r') as file:
        words = [line.strip() for line in file]
    boggle = Boggle(board, words)

    # print full dictionary
    print(boggle.solver())
    
    # print only words
    print(boggle.get_words())

    # print only coords
    print(boggle.get_coords())

    # print word: coord format
    boggle.print_result()

