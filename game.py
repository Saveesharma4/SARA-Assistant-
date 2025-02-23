import random

def play():
    print("Starting the game...")
    
    youDict = {"S": 1, "W": -1, "G": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    while True:  # Infinite loop to keep the game running
        youstr = input("Enter your choice (S for Snake, W for Water, G for Gun) or type 'STOP' to exit: ").upper()

        if youstr == "STOP":
            print("Exiting the game...")
            break  # Exit the loop when the user types "STOP"

        if youstr not in youDict:
            print("Invalid choice! Please enter S, W, G, or STOP.")
            continue  # Restart the loop if input is invalid

        computer = random.choice([-1, 0, 1])
        you = youDict[youstr]

        # Display choices
        print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

        # Determine result
        if computer == you:
            print("It's a draw!")
        elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
            print("You lose!")
        else:
            print("You win!")

# Prevents the game from running automatically when imported
if __name__ == "__main__":
    play()
