from pyggle import Boggle, time, score

if __name__ == "__main__":
    board = "isuo osve nepa ntsu"

    with open('sample_data.txt', 'r') as file:
        words = [line.strip() for line in file]

    boggle = Boggle(board, words, True)# print time to solve boggle board

    print(time(boggle)) # roughly 0.01 seconds

    print(sum(score(boggle))) # 30
