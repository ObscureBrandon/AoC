from typing import TypedDict

with open("input.txt") as f:
    strategy = [line.split() for line in f.read().strip().splitlines()]

# A X ROCK 1
# B Y PAPER 2
# C Z SCISSORS 3

# 0 for loss
# 3 for draw
# 6 for win

class Outcome(TypedDict):
    outcome: int
    fix: str

outcomes: dict[str, Outcome] = {
    "AX": {"outcome": 1 + 3, "fix": "Z"},
    "BX": {"outcome": 1 + 0, "fix": "X"},
    "CX": {"outcome": 1 + 6, "fix": "Y"},
    "AY": {"outcome": 2 + 6, "fix": "X"},
    "BY": {"outcome": 2 + 3, "fix": "Y"},
    "CY": {"outcome": 2 + 0, "fix": "Z"},
    "AZ": {"outcome": 3 + 0, "fix": "Y"},
    "BZ": {"outcome": 3 + 6, "fix": "Z"},
    "CZ": {"outcome": 3 + 3, "fix": "X"},
}

#Part 1
total_score = sum(outcomes[opp + me]["outcome"] for opp, me in strategy)
print(total_score)


#Part 2
#X -> You need to lose
#Y -> You need to draw
#Z -> You need to win
total_score = sum(outcomes[opp + outcomes[opp + me]["fix"]]["outcome"] for opp, me in strategy)
print(total_score)