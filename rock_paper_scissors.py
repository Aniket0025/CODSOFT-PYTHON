import random

youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "rock", -1: "paper", 0: "scissors"}
while True:
    computer = random.choice([-1, 0, 1])  
    
    youstr = input("Enter your choice (r for rock, p for paper, s for scissors, q to quit): ")
    if youstr == "q":
        print("Thanks for playing! Goodbye!")
        break

    if youstr not in youDict:
        print("Invalid input, please enter 'r', 'p', 's', or 'q' to quit.")
        continue

    you = youDict[youstr]

    print(f"\nYou chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

    if (computer == -1 and you == 1):  # paper vs rock
        print("You win!")
    elif (computer == -1 and you == 0):  # paper vs scissors
        print("You lose!")
    elif (computer == 1 and you == -1):  # rock vs paper
        print("You lose!")
    elif (computer == 1 and you == 0):  # rock vs scissors
        print("You win!")
    elif (computer == 0 and you == 1):  # scissors vs rock
        print("You lose!")
    elif (computer == 0 and you == -1):  # scissors vs paper
        print("You win!")
    elif (computer == you):  # Same choice
        print("It's a tie!")
    else:
        print("Something went wrong.")

    print("\n-------------------------\n")
