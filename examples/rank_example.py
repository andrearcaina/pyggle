from pyggle import Boggle, rank

if __name__ == "__main__":
    board = "fpads sghtp anrie tltet eonha"

    boggle = Boggle(board)
    
    # print(rank(boggle)) # will print top 10 words with their scores by default

    # prints top 5 words with their scores (pass in any integer > 0)
    for word, score in rank(boggle, 5):
        print(f"{word}: {score}")