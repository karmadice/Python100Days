import random
import sys

print("Let's play a game of ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0
cpuMove = ""
while True:
    print(f"Wins, Losses, Ties: { wins, losses, ties }")
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print("Please choose r, p, s, or q")

    if playerMove == "r":
        print("ROCK versus...")
    if playerMove == "p":
        print("PAPER versus...")
    if playerMove == "s":
        print("SCISSORS versus...")

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        cpuMove = "r"
        print("ROCK")
    if randomNumber == 2:
        cpuMove = "p"
        print("PAPER")
    if randomNumber == 3:
        cpuMove = "s"
        print("SCISSORS")

    if playerMove == cpuMove:
        print("Its a tie!")
        ties = ties + 1
    if playerMove == "r" and cpuMove == "p":
        print("You loose!")
        losses = losses + 1
    if playerMove == "r" and cpuMove == "s":
        print("You win!")
        wins = wins + 1
    if playerMove == "p" and cpuMove == "r":
        print("You win!")
        wins = wins + 1
    if playerMove == "p" and cpuMove == "s":
        print("You loose!")
        losses = losses + 1
    if playerMove == "s" and cpuMove == "r":
        print("You loose!")
        losses = losses + 1