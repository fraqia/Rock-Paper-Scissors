from random import randint
from fuzzywuzzy import process

def player_hand(hand: str, player_hand_list: list) -> list:
    options = ["Rock", "Paper", "Scissors"]

    try:
        player_choice = 0
        closest_match, score = process.extractOne(hand, options)
        print(f"Closest match: {closest_match} (Score: {score})")
        if score < 92:
            print("Invalid choice! Please try again.")
            return None  
        print((closest_match))
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
        print(player_hand_list)
        return player_hand_list
    except ValueError:
        print("Invalid choice! Please try again.")
        return None  

def computer_hand(c_hand_list) -> list:
    options = {"Rock":1, "Paper":2, "Scissors":3}
    c_hand = randint(1,3)
    for key,value in options.items():
        if c_hand == value:
            c_hand_list.append(key)
            c_hand_list.append(value)
    # print(c_hand_list)
    print(f"Computer:{c_hand_list[0]}")
    return c_hand_list

def who_wins(player_hand_list: list, c_hand_list: list, results: dict) -> dict:
    is_it_draw = False
    if player_hand_list[1] == c_hand_list[1]:
        print("It's a draw.")
        results["Draws"] += 1
        is_it_draw = True
        return results, is_it_draw
    else:
        if player_hand_list[1] == 1: #Rock
            if c_hand_list[1] == 3: # Scissor
                print("You won.")
                results["Wins"] += 1
            elif c_hand_list[1] == 2: #Paper
                print("You lost.")
                results["Loses"] += 1
        elif player_hand_list[1] == 2: #Paper
            if c_hand_list[1] == 1: # Rock
                print("You won.")
                results["Wins"] += 1
            elif c_hand_list[1] == 3: #Scissor
                print("You lost.")
                results["Loses"] += 1
        elif player_hand_list[1] == 3: #Scissor
            if c_hand_list[1] == 2: # Paper
                print("You won.")
                results["Wins"] += 1
            elif c_hand_list[1] == 1: #Rock
                print("You lost.")
                results["Loses"] += 1
        return results, is_it_draw

def results_game(results: dict, player_hand_list: list, c_hand_list: list):
    max_value = max(results.values())
    print("*"*50)
    if results["Wins"] > results["Loses"]:
        print("You won!")
    elif results["Wins"] < results["Loses"]:
        print("You lost!")
    elif results["Wins"] == results["Loses"]:
        print("DRAW!")
    print("Thank you for playing!")
    print("*"*50)

def game(player_hand_list: list, c_hand_list:list, results:dict, rounds_start:int) -> dict:
    results, is_it_draw = who_wins(player_hand_list, c_hand_list, results)
    if is_it_draw == True:
        rounds_start -= 1
    print("*"*50)
    print(f'Result is now:')
    print(f'{"Wins":<8}{"Loses":<8}{"Draws":<8}')
    print(f'{results["Wins"]:<8}{results["Loses"]:<8}{results["Draws"]:<8}')
    return results, rounds_start

if __name__=="__main__":
    while True:
        try:
            results = {"Wins": 0, "Loses": 0, "Draws": 0}

            c_hand_list = []
            rounds = int(input('How many rounds would you like to play?\n'))
            rounds_start = 1
            while rounds_start <= rounds:
                player_hand_list = []
                c_hand_list = []
                print("*"*50)
                print(f"Round {rounds_start}:")
                hand = input('Enter your choice (Rock/Paper/Scissors): ')
                hand = hand.strip()
                player_hand_list = player_hand(hand, player_hand_list)
                if player_hand_list is None:
                    continue
                c_hand_list = computer_hand(c_hand_list)
                results, rounds_start = game(player_hand_list, c_hand_list, results, rounds_start)
                print("rounds")
                print(rounds_start)
                rounds_start += 1
            results_game(results, player_hand_list, c_hand_list)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number of rounds.")
        except Exception as e:
            print(f"An error occurred: {e}")
        # results_game(results, player_hand_list, c_hand_list)



