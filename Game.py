from random import randint
from fuzzywuzzy import process

def player_hand(hand: str, player_hand_list: list) -> list:
    options = ["1. Rock", "2. Paper", "3. Scissors", "Rock", "Paper", "Scissors"]
    # try:
    player_hand = 0
    if hand in ['1', '2', '3']:
        closest_match = options[int(hand) - 1]
        score = 100
        # player_hand_list.append(closest_match)
        # player_hand_list.append(player_hand)
        # return player_hand_list
    else:
        closest_match, score = process.extractOne(hand, options)
    print(f"Closest match: {closest_match} (Score: {score})")
    if score < 95:
        print("Invalid choice! Please try again.")
        return None  
    print((closest_match))
    if closest_match == "1. Rock" or closest_match.lower() == "rock":
        player_hand = 1
        closest_match = "Rock"
    elif closest_match == "2. Paper" or closest_match.lower() == "paper":
        player_hand = 2
        closest_match = "Paper"
    elif closest_match == "3. Scissors" or closest_match.lower() == "scissors":
        player_hand = 3
        closest_match = "Scissors"
    player_hand_list.append(closest_match)
    player_hand_list.append(player_hand)
    # print(player_hand_list)
    print(f'You: {closest_match}')
    print(player_hand_list)
    return player_hand_list
    # except ValueError:
    #     print("Invalid choice! Please try again.")
    #     return None  

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
    if player_hand_list[1] == c_hand_list[1]:
        print("It's a draw.")
        results["Draws"] += 1
        return results
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
        return results

def results_game(results: dict, player_hand_list: list, c_hand_list: list):
    if len(set(results.values())) == 1:
        print("Need one more game to decide the victor")
        hand = input('Enter your choice: (1.Rock/2.Paper/3.Scissors)')
        player_hand_list = player_hand(hand, player_hand_list)
        if player_hand_list is None:
            return
        c_hand_list = computer_hand(c_hand_list)
        results = game(player_hand_list, c_hand_list, results)
    max_value = max(results.values())
    max_keys = [key for key, value in results.items() if value == max_value]
    max_keys = "".join(max_keys)
    # print(max_keys, max_value)
    print("*"*50)
    if max_keys == "Wins":
        print("You won!")
    elif max_keys == "Loses":
        print("You lost!")
    else:
        print("DRAW!")
    print("Thank you for playing!")
    print("*"*50)

def game(player_hand_list: list, c_hand_list:list, results:dict):
    results = who_wins(player_hand_list, c_hand_list, results)
    print("*"*50)
    print(f'Result is now:')
    for key,value in results.items():
        print(f'{key}: {value}')
    return results

if __name__=="__main__":
    while True:
        try:
            results = {"Wins": 0, "Loses": 0, "Draws": 0}
            player_hand_list = []
            c_hand_list = []
            rounds = int(input('How many rounds would you like to play?\n'))
            rounds_start = 1
            while rounds_start <= rounds:
                print("*"*50)
                print(f"Round {rounds_start}:")
                hand = input('Enter your choice (1.Rock/2.Paper/3.Scissors): ')
                player_hand_list = player_hand(hand, player_hand_list)
                if player_hand_list == None:
                    continue
                c_hand_list = computer_hand(c_hand_list)
                results = game(player_hand_list, c_hand_list, results)
                rounds_start += 1
                player_hand_list = []
                c_hand_list = []
            results_game(results, player_hand_list, c_hand_list)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number of rounds.")
        except Exception as e:
            print(f"An error occurred: {e}")
        # results_game(results, player_hand_list, c_hand_list)



