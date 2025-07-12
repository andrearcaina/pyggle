from .boggle import Boggle

# functions for pythonic function calls
def solve(boggle: Boggle) -> dict[str, list[tuple[int]]]:
    return boggle.solve()

def time(boggle: Boggle) -> float:
    return boggle.time_solve()

def words(boggle: Boggle) -> list[str]:
    return boggle.get_words()

def coords(boggle: Boggle) -> list[tuple[int, int]]:
    return boggle.get_coords()

def score(boggle: Boggle) -> list[int]:
    return boggle.get_score()