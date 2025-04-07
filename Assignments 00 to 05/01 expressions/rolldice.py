import random

one_side = 6
def roll_dice():
    die1 = random.randint(1, one_side)
    die2 = random.randint(1, one_side)
    # Get their total
    total = die1 + die2
   
   # Print out the results
    print("Dice have", one_side, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

roll_dice()


