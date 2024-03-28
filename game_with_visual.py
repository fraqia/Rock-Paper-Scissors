import pygame
import sys
from random import randint

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors Game")

# Load images
rock_image = pygame.image.load("rock.png")
paper_image = pygame.image.load("paper.png")
scissors_image = pygame.image.load("scissors.png")

# Define fonts
font = pygame.font.Font(None, 36)

def draw_text(text, color, x, y, height):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y + height)
    screen.blit(text_surface, text_rect)

def generate_computer_choice():
    return randint(1, 3)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
        return "Player wins"
    else:
        return "Computer wins"

def player_hand(player_hand_list: list, rock_rect, paper_rect, scissors_rect) -> list:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rock_rect.collidepoint(mouse_pos):
                player_hand_list.append("Rock")
                player_hand_list.append(1)
                return player_hand_list

            elif paper_rect.collidepoint(mouse_pos):
                player_hand_list.append("Paper")
                player_hand_list.append(2)
                return player_hand_list
            
            elif scissors_rect.collidepoint(mouse_pos):
                player_hand_list.append("Scissors")
                player_hand_list.append(3)
                return player_hand_list
    return None

def edit_text(player_choice, computer_choice):
    if player_choice == 1:
        player_choice = "Rock"
    elif player_choice == 2:
        player_choice = "Paper"
    elif player_choice == 3:
        player_choice = "Scissors"
    if computer_choice == 1:
        computer_choice = "Rock"
    elif computer_choice == 2:
        computer_choice = "Paper"
    elif computer_choice == 3:
        computer_choice = "Scissors"
    return player_choice, computer_choice

def main_game_loop():
    #draw the images on the screen
    rock_rect = screen.blit(pygame.transform.scale(rock_image, (150, 150)), (50, 200))
    paper_rect = screen.blit(pygame.transform.scale(paper_image, (150, 150)), (300, 200))
    scissors_rect = screen.blit(pygame.transform.scale(scissors_image, (150, 150)), (550, 200))

    result_image = None
    result_timer = None

    while True:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if rock_rect.collidepoint(mouse_pos):
                    player_choice = 1  # Rock
                elif paper_rect.collidepoint(mouse_pos):
                    player_choice = 2  # Paper
                elif scissors_rect.collidepoint(mouse_pos):
                    player_choice = 3  # Scissors

                computer_choice = generate_computer_choice()
                winner = determine_winner(player_choice, computer_choice)

                #clear the screen
                screen.fill((255, 255, 255))
                screen.blit(rock_image, (50, 200))
                screen.blit(paper_image, (300, 200))
                screen.blit(scissors_image, (550, 200))

                player_choice, computer_choice = edit_text(player_choice, computer_choice)

                draw_text(f"Player choice: {player_choice}", (0, 0, 0), 50, 100, 0)
                draw_text(f"Computer choice: {computer_choice}", (0, 0, 0), 50, 150, 0)
                draw_text(f"Winner: {winner}", (255, 0, 0), 50, 250, 100)


        player_hand_list = []
        player_hand_list = player_hand(player_hand_list, rock_rect, paper_rect, scissors_rect)

        if player_hand_list:
            print(f'You: {player_hand_list[0]}')

        pygame.display.flip()
            
            
main_game_loop()