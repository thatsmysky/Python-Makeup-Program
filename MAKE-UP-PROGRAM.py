# Lucy Kull
# Professor Hare
# Make-Up Program

import random

# What can the dice roll?
G_outcomes = ["BRAINS", "BRAINS", "BRAINS", "RUNNER", "RUNNER", "SHOTGUN"]
Y_outcomes = ["BRAINS", "BRAINS", "RUNNER", "RUNNER", "SHOTGUN", "SHOTGUN"]
R_outcomes = ["BRAINS", "RUNNER", "RUNNER", "SHOTGUN", "SHOTGUN", "SHOTGUN"]
points_gained = 0

# How we show the score
def show_score(score):
    print("\nSCORE\n")
    if numberofplayers == 2:
        print("{:>10} {:>10}".format(Player1, Player2))
        print("{:>10} {:>10}".format(score[Player1], score[Player2]))
    if numberofplayers == 3:
        print("{:>10} {:>10} {:>10}".format(Player1, Player2, Player3))
        print("{:>10} {:>10} {:>10}".format(score[Player1], score[Player2], score[Player3]))
    if numberofplayers == 4:
        print("{:>10} {:>10} {:>10} {:>10}".format(Player1, Player2, Player3, Player4))
        print("{:>10} {:>10} {:>10} {:>10}".format(score[Player1], score[Player2], score[Player3], score[Player4]))


def roll_my_dice(dice1):
    # We roll a lot, let's make that a function
    points_gained = 0
    for d in dice1:
        if d in "G":
            # Keep track of what you rolled
            player_roll.append(random.sample(G_outcomes, 1))
            if player_roll[-1][0] not in "RUNNER":
                # Get rid of the dice you keep
                Dice.remove("G")
                Used_Dice.append("G")
        if d in "Y":
            player_roll.append(random.sample(Y_outcomes, 1))
            if player_roll[-1][0] not in "RUNNER":
                Dice.remove("Y")
                Used_Dice.append("Y")
        if d in "R":
            player_roll.append(random.sample(R_outcomes, 1))
            if player_roll[-1][0] not in "RUNNER":
                Dice.remove("R")
                Used_Dice.append("R")
    # Let the player know what they rolled
    print("{} rolled {}\n".format(Turn, player_roll))
    for r in player_roll:
        for w in r:
            if w in "BRAINS":
                # Keep score
                score[Turn] += 1
                points_gained += 1
            if w in "SHOTGUN":
                # When you get shot, it adds up
                Shot[t] += 1
    return player_roll, points_gained

PlayOn = True
TakeTurn = True
# Let's boogie
while PlayOn:
    t = 0
    # These are our dice
    Dice = ["G", "G", "G", "G", "G", "G", "Y", "Y", "Y", "Y", "R", "R", "R"]
    Used_Dice = []
    # How many people do we have to deal with?
    numberofplayers = int(input("How many players? \n"))
    if numberofplayers < 2:
        print("please enter a number between 2 and 4\n")
        continue
    if numberofplayers > 4:
        print("please enter a number between 2 and 4\n")
        continue
    # Let's name these players
    Player1 = input("Player One name: ")
    Player2 = input("Player Two name: ")
    score = {Player1: 0, Player2: 0}
    Players = [Player1, Player2]
    if numberofplayers >= 3:
        Player3 = input("Player Three name: ")
        score[Player3] = 0
        Players.append(Player3)
    if numberofplayers == 4:
        Player4 = input("Player Four name: ")
        score[Player4] = 0
        Players.append(Player4)
    show_score(score)
    Shot = [0, 0, 0, 0, 0]
    # This is how you take turns
    while TakeTurn:
        # When everyone has played:
        if t >= numberofplayers:
            print("Everyone has gone!\n")
            t = 0
            Shot = [0, 0, 0, 0, 0]
        Turn = Players[t]
        # If someone wins:
        if score[Turn] > 13:
            print(Turn, "won!\n")
            break
        player_roll = []
        player_dice = random.sample(Dice, 3)
        # Roll!
        roll_my_dice(player_dice)
        #3Let the player know what they're getting into
        print(Turn, "has been shot {} times, 3 times and their turn is over\n".format(Shot[t]))
        print(Turn, "has kept {} dice, they were {}\n".format(len(Used_Dice), Used_Dice))
        print("In the bag, there are {} dice\n".format(Dice))
        # Scores matter
        show_score(score)
        # You get shot too many times, you die (in a zombie way)
        if Shot[t] >= 3:
            print(Turn, "has died!\n")
            score[Turn] -= points_gained
            t += 1
            Dice.extend(Used_Dice)
            Used_Dice = []
            points_gained = 0
            continue
        # Honestly I had a problem with being too good at this game where I'd roll all the dice
        if len(Dice) < 3:
            print("You have used all the dice.\n")
            Dice.extend(Used_Dice)
            Used_Dice = []
            t += 1
            points_gained = 0
            continue
        # Keep this party going!
        Roll_Again = input("\nWould you like to roll again? \n")
        Roll_Again = Roll_Again.upper()
        if Roll_Again not in "Y" "N":
            print("Please answer Yes or No\n")
        if Roll_Again in "Y":
            TakeTurn = True
        else:
            TakeTurn = True
            # continue ont he the next player
            t += 1
            Dice.extend(Used_Dice)
            Used_Dice = []
            points_gained = 0
    else:
        show_score(score)
        # Play again?
        PlayAgain = input("Would you like to play again? \n")
        if PlayAgain not in "Y" "N":
            print("You have to choose\n")
        if PlayAgain in "Y":
            PlayOn = True
        else:
            PlayOn = False
            break
