from random import randint
from fuzzywuzzy import process

def open_new_file() -> None:
    with open("Game_Record.txt","w") as file:
        pass

def player_hand(hand: str, player_hand_list: list) -> list:
    options = ["Rock", "Paper", "Scissors"]

    try:
        player_choice = 0
        closest_match, score = process.extractOne(hand, options)
        # print(f"Closest match: {closest_match} (Score: {score})")
        if score < 92:
            print("Invalid choice! Please try again.\n")
            return None  
        # print((closest_match))
        if closest_match.lower() == "rock":
            player_choice = 1
            closest_match = "Rock"
        elif closest_match.lower() == "paper":
            player_choice = 2
            closest_match = "Paper"
        elif closest_match.lower() == "scissors":
            player_choice = 3
            closest_match = "Scissors"
        player_hand_list.append(closest_match)
        player_hand_list.append(player_choice)
        # print(player_hand_list)
        print(f'You: {closest_match}')
        # print(player_hand_list)
        return player_hand_list
    except ValueError:
        print("Invalid choice! Please try again.\n")
        return None  

def computer_hand(c_hand_list) -> list:
    options = {"Rock":1, "Paper":2, "Scissors":3}
    c_hand = randint(1,3)
    for key,value in options.items():
        if c_hand == value:
            c_hand_list.append(key)
            c_hand_list.append(value)
    # print(c_hand_list)
    print(f"Computer: {c_hand_list[0]}")
    return c_hand_list

def game_scores(player_hand_list: list, c_hand_list:list, results:dict, rounds_start:int) -> dict:
    results, is_it_draw = who_wins(player_hand_list, c_hand_list, results)
    if is_it_draw == True:
        rounds_start -= 1
    print("Result is now:")
    print("=" * 23)
    print(f'{"Wins":<8}|{"Loses":<8}|{"Draws":<8}')
    print(f'{results["Wins"]:<8}|{results["Loses"]:<8}|{results["Draws"]:<8}')
    save_into_file(results)
    # print("_" * 50)
    return results, rounds_start

def who_wins(player_hand_list: list, c_hand_list: list, results: dict) -> dict:
    is_it_draw = False
    if player_hand_list[1] == c_hand_list[1]:
        print("It's a draw.\n")
        results["Draws"] += 1
        is_it_draw = True
        return results, is_it_draw
    else:
        if player_hand_list[1] == 1: #Rock
            if c_hand_list[1] == 3: # Scissor
                print("You won.\n")
                results["Wins"] += 1
            elif c_hand_list[1] == 2: #Paper
                print("You lost.\n")
                results["Loses"] += 1
        elif player_hand_list[1] == 2: #Paper
            if c_hand_list[1] == 1: # Rock
                print("You won.\n")
                results["Wins"] += 1
            elif c_hand_list[1] == 3: #Scissor
                print("You lost.\n")
                results["Loses"] += 1
        elif player_hand_list[1] == 3: #Scissor
            if c_hand_list[1] == 2: # Paper
                print("You won.\n")
                results["Wins"] += 1
            elif c_hand_list[1] == 1: #Rock
                print("You lost.\n")
                results["Loses"] += 1
        return results, is_it_draw

def save_into_file(results: str):
    with open("Game_Record.txt","a") as file:
        file.write("=" * 23)
        file.write(f'\n{"Wins":<8}|{"Loses":<8}|{"Draws":<8}\n')
        file.write(f'{results["Wins"]:<8}|{results["Loses"]:<8}|{results["Draws"]:<8}\n')
        file.write("\n")

def game_winner(results: dict) -> None:
    print("*"*50)
    if results["Wins"] > results["Loses"]:
        print("You won!")
    elif results["Wins"] < results["Loses"]:
        print("You lost!")
    elif results["Wins"] == results["Loses"]:
        print("DRAW!")
    winning_percentage(results)
    print("Thank you for playing!")
    print("*"*50)

def winning_percentage(results: dict):
    matches = int(results["Wins"]) + int(results["Loses"] + int(results["Draws"]))
    win_percent = (int(results["Wins"]) / matches)*100
    print(f'Winning percentage: {win_percent}%')

if __name__=="__main__":
    open_new_file()
    while True:
        try:
            results = {"Wins": 0, "Loses": 0, "Draws": 0}

            c_hand_list = []
            rounds = int(input('How many rounds would you like to play? '))
            rounds_start = 1
            while rounds_start <= rounds:
                player_hand_list = []
                c_hand_list = []
                print("*"*50)
                # print(f"Round {rounds_start}:")
                hand = input('Enter your choice (Rock/Paper/Scissors): ')
                print()
                hand = hand.strip()
                player_hand_list = player_hand(hand, player_hand_list)
                if player_hand_list is None:
                    continue
                c_hand_list = computer_hand(c_hand_list)
                results, rounds_start = game_scores(player_hand_list, c_hand_list, results, rounds_start)
                print()
                print()
                rounds_start += 1
            game_winner(results)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number of rounds.")
        except Exception as e:
            print(f"An error occurred: {e}")




