from pyggle import Boggle 
import timeit

if __name__ == "__main__":
    board = "ea st"
    # board can be [["e", "a"], ["s", "t"]] or "ea st"
    
    # this is only 3000 words, but the web demo will utilize all 479k words
    with open('sample_data.txt', 'r') as file:
        words = [line.strip() for line in file]
    
    # the second and third argument are optional
    # if words is not given, will default to 479k word list
    # if official is not given, will default to False (will return all words, regardless of length)
    # official means "official rules of Boggle game"
    boggle = Boggle(board, words, True)

    # print time to solve boggle board
    print(boggle.time_solve()) # roughly 0.001 seconds

    # print full dictionary
    print(boggle.solver())
    
    # print only words
    print(boggle.get_words())

    # print only coords
    print(boggle.get_coords())

    # get length of boggle
    print(boggle.get_length()) # 4    

    # get total score
    print(sum(boggle.get_score())) # 6

    # print word: coord format
    boggle.print_result()
