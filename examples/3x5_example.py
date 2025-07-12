from pyggle import Boggle, time, score

if __name__ == "__main__":
    board = "aesob fghik lmtrs"

    boggle = Boggle(board, None, True)

    print(time(boggle)) # 1.13 seconds

    print(sum(score(boggle))) # 209
