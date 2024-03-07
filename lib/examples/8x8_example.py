from pyggle import Boggle

if __name__ == "__main__":
    board = [["o", "c", "n", "e", "a", "s", "r", "a"],
            ["c", "r", "i", "s", "h", "t", "i", "r"],
            ["l", "l", "a", "n", "n", "r", "e", "n"],
            ["g", "e", "n", "s", "s", "a", "q", "n"],
            ["d", "a", "m", "c", "o", "b", "n", "u"],
            ["n", "r", "o", "o", "s", "y", "e", "n"],
            ["a", "t", "s", "a", "r", "s", "o", "n"],
            ["b", "e", "s", "s", "n", "n", "i", "s"]]

    boggle = Boggle(board, None, True)

    print(boggle.time_solve()) # roughly 7.6 seconds

    print(boggle.get_score()) # 5567