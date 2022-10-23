from random import randint
def rps_match(p1, p2):
    if p1 == 0 and p2 == 0:
        return 0
    elif p1 == 0 and p2 == 1:
        return 2
    elif p1 == 0 and p2 == 2:
        return 1
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
def init():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    option = [rock, paper, scissors]
    ROUND_1 = True
    ROUND_2 = False
    ROUND_3 = False
    ROUND_4 = False
    ROUND_5 = False
    draw = """    
██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
██║░░██║██╔══██╗██╔══██║░░████╔═████║░
██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░"""
    game_result = [draw, "You WON ✨✨✨ !!", "Bot WON 💀💀💀 !!"]
    series_won = "Congratulation, you won the game!! 🎉🎉🎉"
    series_lost = "Unfortunately, you lost the game!!! ❌❌❌ Better luck next time 🥺"
    p1_score = 0
    p2_score = 0
    while ROUND_1:
        p2 = randint(0, 2)
        print("Welcome to round 1")
        print(f"Score: User 🤓 = {p1_score}  Bot 🤖 = {p2_score} ")
        print("Please choose your option, {0 = rock, 1 = paper, 2 = scissors}")
        p1 = input("Enter your option: ")
        try:
            p1 = int(p1)
        except ValueError:
            print("Invalid input! Make sure valid option is used")
            print("The game is restarting !! ⌛")
            continue
        if p1 > 2 or p1 < 0:
            print("Invalid input! Make sure valid option is used")
            print("The game is restarting !! ⌛")
            continue
        else:
            print(option[int(p1)])
            print("🤓's choice")
            print("-------------------------------")
            print("🤖's choice")
            print(option[int(p2)])
            result = rps_match(int(p1), int(p2))
            print(game_result[int(result)])
            if result == 0:
                continue
            elif result == 1:
                p1_score = p1_score + 1
                ROUND_2 = True
            elif result == 2:
                p2_score = p2_score + 1
                ROUND_2 = True
            while ROUND_2:
                p2 = randint(0, 2)
                print("Welcome to round 2")
                print(f"Score: User 🤓 = {p1_score}  Bot 🤖 = {p2_score} ")
                print("Please choose your option, {0 = rock, 1 = paper, 2 = scissors}")
                p1 = input("Enter your option: ")
                try:
                    p1 = int(p1)
                except ValueError:
                    print("Invalid input! Make sure valid option is used")
                    print("The game is restarting !! ⌛")
                    continue
                if p1 > 2 or p1 < 0:
                    print("Invalid input! Make sure valid option is used")
                    print("The game is restarting !! ⌛")
                    continue
                else:
                    print(option[int(p1)])
                    print("🤓's choice")
                    print("-------------------------------")
                    print("🤖's choice")
                    print(option[int(p2)])
                    result = rps_match(int(p1), int(p2))
                    print(game_result[int(result)])
                if result == 0:
                    continue
                elif result == 1:
                    p1_score = p1_score + 1
                    ROUND_3 = True
                elif result == 2:
                    p2_score = p2_score + 1
                    ROUND_3 = True
                while ROUND_3:
                    p2 = randint(0, 2)
                    print("Welcome to round 3")
                    print(f"Score: User 🤓 = {p1_score}  Bot 🤖 = {p2_score} ")
                    print("Please choose your option, {0 = rock, 1 = paper, 2 = scissors}")
                    p1 = input("Enter your option: ")
                    try:
                        p1 = int(p1)
                    except ValueError:
                        print("Invalid input! Make sure valid option is used")
                        print("The game is restarting !! ⌛")
                        continue
                    if p1 > 2 or p1 < 0:
                        print("Invalid input! Make sure valid option is used")
                        print("The game is restarting !! ⌛")
                        continue
                    else:
                        print(option[int(p1)])
                        print("🤓's choice")
                        print("-------------------------------")
                        print("🤖's choice")
                        print(option[int(p2)])
                        result = rps_match(int(p1), int(p2))
                        print(game_result[int(result)])
                        if result == 0:
                            continue
                        elif result == 1:
                            p1_score = p1_score + 1
                            if p1_score == 3:
                                print(f"The score is {p1_score} to {p2_score} !!")
                                print(series_won)
                                while True:
                                    again = input("Type \"Yes\" or \"No\" to play again: ")
                                    if again.upper() == "YES":
                                        init()
                                    elif again.upper() == "NO":
                                        print("Thank you for playing this game!!! 🙏🙏🙏")
                                        exit()
                                    else:
                                        print("Please enter \"Yes\" or \"No\"")
                                        continue
                            else:
                                ROUND_4 = True
                        elif result == 2:
                            p2_score = p2_score + 1
                            if p2_score == 3:
                                print(f"The score is {p1_score} to {p2_score} !!")
                                print(series_lost)
                                while True:
                                    again = input("Type \"Yes\" or \"No\" to play again: ")
                                    if again.upper() == "YES":
                                        init()
                                    elif again.upper() == "NO":
                                        print("Thank you for playing this game!!! 🙏🙏🙏")
                                        exit()
                                    else:
                                        print("Please enter \"Yes\" or \"No\"")
                                        continue
                            else:
                                ROUND_4 = True
                    while ROUND_4:
                        p2 = randint(0, 2)
                        print("Welcome to round 4")
                        print(f"Score: User 🤓 = {p1_score}  Bot 🤖 = {p2_score} ")
                        print("Please choose your option, {0 = rock, 1 = paper, 2 = scissors}")
                        p1 = input("Enter your option: ")
                        try:
                            p1 = int(p1)
                        except ValueError:
                            print("Invalid input! Make sure valid option is used")
                            print("The game is restarting !! ⌛")
                            continue
                        if p1 > 2 or p1 < 0:
                            print("Invalid input! Make sure valid option is used")
                            print("The game is restarting !! ⌛")
                            continue
                        else:
                            print(option[int(p1)])
                            print("🤓's choice")
                            print("-------------------------------")
                            print("🤖's choice")
                            print(option[int(p2)])
                            result = rps_match(int(p1), int(p2))
                            print(game_result[int(result)])
                            if result == 0:
                                continue
                            elif result == 1:
                                p1_score = p1_score + 1
                                if p1_score == 3:
                                    print(f"The score is {p1_score} to {p2_score} !!")
                                    print(series_won)
                                    while True:
                                        again = input("Type \"Yes\" or \"No\" to play again: ")
                                        if again.upper() == "YES":
                                            init()
                                        elif again.upper() == "NO":
                                            print("Thank you for playing this game!!! 🙏🙏🙏")
                                            exit()
                                        else:
                                            print("Please enter \"Yes\" or \"No\"")
                                            continue
                                else:
                                    ROUND_5 = True
                            elif result == 2:
                                p2_score = p2_score + 1
                                if p2_score == 3:
                                    print(f"The score is {p1_score} to {p2_score} !!")
                                    print(series_lost)
                                    while True:
                                        again = input("Type \"Yes\" or \"No\" to play again: ")
                                        if again.upper() == "YES":
                                            init()
                                        elif again.upper() == "NO":
                                            print("Thank you for playing this game!!! 🙏🙏🙏")
                                            exit()
                                        else:
                                            print("Please enter \"Yes\" or \"No\"")
                                            continue
                                else:
                                    ROUND_5 = True
                        while ROUND_5:
                            p2 = randint(0, 2)
                            print("Welcome to the final round!!!")
                            print(f"Score: User 🤓 = {p1_score}  Bot 🤖 = {p2_score} ")
                            print("DO OR DIE SITUATION!!")
                            print("Please choose your option, {0 = rock, 1 = paper, 2 = scissors}")
                            p1 = input("Enter your option: ")
                            try:
                                p1 = int(p1)
                            except ValueError:
                                print("Invalid input! Make sure valid option is used")
                                print("The game is restarting !! ⌛")
                                continue
                            if p1 > 2 or p1 < 0:
                                print("Invalid input! Make sure valid option is used")
                                print("The game is restarting !! ⌛")
                                continue
                            else:
                                print(option[int(p1)])
                                print("🤓's choice")
                                print("-------------------------------")
                                print("🤖's choice")
                                print(option[int(p2)])
                                result = rps_match(int(p1), int(p2))
                                print(game_result[int(result)])
                                if result == 0:
                                    continue
                                elif result == 1:
                                    p1_score = p1_score + 1
                                    if p1_score == 3:
                                        print(f"The score is {p1_score} to {p2_score} !!")
                                        print(series_won)
                                        while True:
                                            again = input("Type \"Yes\" or \"No\" to play again: ")
                                            if again.upper() == "YES":
                                                init()
                                            elif again.upper() == "NO":
                                                print("Thank you for playing this game!!! 🙏🙏🙏")
                                                exit()
                                            else:
                                                print("Please enter \"Yes\" or \"No\"")
                                                continue
                                elif result == 2:
                                    p2_score = p2_score + 1
                                    if p2_score == 3:
                                        print(f"The score is {p1_score} to {p2_score} !!")
                                        print(series_lost)
                                        while True:
                                            again = input("Type \"Yes\" or \"No\" to play again: ")
                                            if again.upper() == "YES":
                                                init()
                                            elif again.upper() == "NO":
                                                print("Thank you for playing this game!!! 🙏🙏🙏")
                                                exit()
                                            else:
                                                print("Please enter \"Yes\" or \"No\"")
                                                continue
init()









