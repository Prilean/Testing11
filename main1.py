import random
def rps_match(p1, p2):
    if p1 == 0 and p2 == 0:
        return 0
    elif p1 == 0 and p2 == 1:
        return 1
    elif p1 == 0 and p2 == 2:
        return 2
    elif p1 == 1 and p2 == 0:
        return 1
    elif p1 == 1 and p2 == 1:
        return 0
    elif p1 == 1 and p2 == 2:
        return 2
    elif p1 == 2 and p2 == 0:
        return 2
    elif p1 == 2 and p2 == 1:
        return 1
    elif p1 == 2 and p2 == 2:
        return 0

user_choice = input("Enter your decision: ")
robot_choice = [0, 1, 2]
decision = rps_match(int(user_choice), int(random.choice(robot_choice)))
if decision == 0:
    print(" ITS FUCKING DRAW !!")
elif decision == 1:
    print(" USER'S EASIEST WIN !!")
else:
    print(" BOT IS BETTER THAN YOU LOL !!")
