from pyggle import Boggle, time, score

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

    print(time(boggle)) # roughly 6.37 seconds

    print(sum(score(boggle))) # 5686
