from pyggle import Boggle

if __name__ == "__main__":
    board = "isuo osve nepa ntsu"

    with open('sample_data.txt', 'r') as file:
        words = [line.strip() for line in file]

    boggle = Boggle(board, words, True)

    print(boggle.time_solve()) # roughly 0.02

    print(sum(boggle.get_score())) # 30
