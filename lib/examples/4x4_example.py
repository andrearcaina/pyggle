from pyggle import Boggle
import timeit

if __name__ == "__main__":
    board = "isuo osve nepa ntsu"

    with open('sample_data.txt', 'r') as file:
        words = [line.strip() for line in file]

    boggle = Boggle(board, words, True)

    boggle.print_result()
    
    print(boggle.time_solve())