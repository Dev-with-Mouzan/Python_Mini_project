import random

def roll_dice():
    min_val = 1
    max_val = 6
    
    while True:
        print("\nRolling the dice...")
        val = random.randint(min_val, max_val)
        print(f"You rolled a {val}")
        
        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    print("Dice Rolling Simulator")
    roll_dice()
