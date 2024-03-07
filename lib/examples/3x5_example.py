from pyggle import Boggle

if __name__ == "__main__":
    board = "aesob fghik lmtrs"

    boggle = Boggle(board, None, True)

    print(boggle.time_solve()) # 1.26 seconds

    print(boggle.get_score()) # 209
