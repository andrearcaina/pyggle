from pyggle import Boggle, time

if __name__ == "__main__":
    boggle = Boggle("aqa dsf", None, True)

    # the letter "q" now represents "qu" in official rules
    boggle.print_result()

    print(time(boggle)) # about 0.13 seconds