from pyggle import Boggle

if __name__ == "__main__":
    board = "aesob fghik lmtrs"

    boggle = Boggle(board, None, True)

    print(boggle.time_solve()) # 1.13 seconds

    print(sum(boggle.get_score())) # 209
