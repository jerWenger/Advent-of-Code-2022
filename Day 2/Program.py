

with open('Day 2/Input.txt') as f:
    first = f.readlines()

#A for Rock, B for Paper, and C for Scissors.
#X for Rock, Y for Paper, and Z for Scissors
#(1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
score = 0

table = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1,"B Y": 5,"B Z": 9,"C X": 7,"C Y": 2,"C Z": 6}

for lines in first:
    
    score += table[lines[:-1]]




# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

cheat = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1,"B Y": 5,"B Z": 9,"C X": 2,"C Y": 6,"C Z": 7}

with open('Day 2/Final.txt') as f:
    second = f.readlines()    

this_score = 0

for lines in second:
    this_score += cheat[lines[:-1]]

print(this_score)