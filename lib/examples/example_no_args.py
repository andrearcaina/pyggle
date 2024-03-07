from pyggle import Boggle 

if __name__ == "__main__":
    board = [['e', 'a'], ['s', 't']]
    
    # given no words, will use 479k word list instead
    boggle = Boggle(board)

    boggle.print_result()

    print(boggle.time_solve()) # 0.08 seconds