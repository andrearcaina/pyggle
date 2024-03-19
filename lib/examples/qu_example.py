import pyggle as py

boggle = py.Boggle("aqa dsf", [], True)

boggle.print_result()

print(boggle.time_solve()) # about 0.13 seconds