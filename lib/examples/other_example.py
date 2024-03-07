from pyggle import Boggle 

if __name__ == "__main__":
    board = "ea st"

    with open('sample_data.txt', 'r') as file:
        words = [line.strip() for line in file]

    boggle = Boggle(board, words)

    # converting to a string
    string_boggle = str(boggle)

    # printing out a visual representation of the boggle board
    print(string_boggle)

    # print boggle board (will print just like the string_boggle above)
    print(boggle)

    # getting first row of boggle board
    print(boggle[0])

    # getting char at position (0,0)
    print(boggle[0][0])

    # getting length of boggle board using len instead of get_length()
    print(len(boggle))

    # conditionals: checking if a word is found in the boggle board
    if "seat" in boggle:
        print("The word 'seat' is in the board")
    else:
        print("The word 'seat' is not in the board")

    if "word" in boggle:
        print("The word 'word' is in the board")
    else:
        print("The word 'word' is not in the board")

    # creates a string representation of boggle (with repr), recreates boggle (with eval), and prints it as
    # a visual representation of the boggle board (with print)
    print(eval(repr(boggle)))