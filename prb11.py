userChoice = input("User choice (rock/paper/scissors or quit): ")
while True:
    userChoice = input("User choice (rock/paper/scissors or quit): ")
    if userChoice == "quit":
        break
    elif userChoice == "rock":
        print("Round 1: You chose: rock | Computer: scissors→ You win!")
        continue
    elif userChoice == "scissors":
        print("Round 3: You chose: scissors | Computer:paper → You win!")
        continue
    elif userChoice == "paper":
        print("Round 2: You chose: paper | Computer: rock →You win!")
        continue