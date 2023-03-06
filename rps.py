# File created by: Kevin Li
 
# import libraries
from time import sleep
from random import randint 
import pygame as pg
import os

# Possible choices for user/computer
choices0 = ["Rock", "Paper", "Scissors"]

# Stats variables
computer_win = 0
user_win = 0
game_tie = 0

# Folder where image files are
game_folder = os.path.dirname(__file__)

# game settings
WIDTH = 1100
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Render results and stats text on the surface
def print_result(result_text, stats_text):
    # Create a pg font object
    font = pg.font.Font(None, 36)

    # Render the result text
    result_text_surface = font.render(result_text, True, (255, 255, 255))

    # Blit the result text surface onto the display surface
    screen.blit(result_text_surface, (WIDTH/2 - result_text_surface.get_width()/2, HEIGHT/2 + 200 - result_text_surface.get_height()/2))

    # Render the stats text
    stats_text_surface = font.render(stats_text, True, (255, 255, 255))

    # Blit the stats text surface onto the display surface
    screen.blit(stats_text_surface, (WIDTH/2 - stats_text_surface.get_width()/2, HEIGHT/2 + 250 - stats_text_surface.get_height()/2))

    # Update the display
    pg.display.update()

# Let the computer randomly choose from choices0
def cpu_randchoice():
    print("computer randomly decides...")
    return choices0[randint(0,2)]

# Compare the user's choice to the computer's choice, decide who won
def compare(user):
    global computer_win , user_win , game_tie

    # Get the computer's choice
    cpu = cpu_randchoice()
    output_text = "the computer chose " + cpu + ", you chose " + user
    print("the computer chose ", cpu)
    print("you chose " + user)

    # Check different scenarios and decide who won
    # Update stats values (win/lose/tie)
    if user == cpu:
        output_text = output_text + ", you tied!"
        game_tie = game_tie + 1
    elif user == "Rock" and cpu == "Scissors":
        output_text = output_text + ", you won!"
        user_win = user_win + 1
    elif user == "Paper" and cpu == "Rock":
        output_text = output_text + ", you won!"
        user_win = user_win + 1
    elif user == "Scissors" and cpu == "Paper":
        output_text = output_text + ", you won!"
        user_win = user_win + 1
    elif cpu == "Rock" and user == "Scissors":
        output_text = output_text + ", you lost!"
        computer_win = computer_win + 1
    elif cpu == "Paper" and user == "Rock":
        output_text = output_text + ", you lost!"
        computer_win = computer_win + 1
    elif cpu == "Scissors" and user == "Paper":
        output_text = output_text + ", you lost!"
        computer_win = computer_win + 1
    else:
        output_text = output_text + " $$$there was an error$$$"
    screen.fill(BLACK)
    # Construct stats text to be displayed
    stats_text = "user wins : " + str(user_win) + "    computer wins : " + str(computer_win) + "    ties : " + str(game_tie)
    print_result(output_text , stats_text )
    
# Initialize pygame
pg.init()
pg.mixer.init()

# Initialize screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()

# Load images to surface at certain locations
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
rock_image_rect.x = 50
rock_image_rect.y = 100

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = 300
paper_image_rect.y = 100

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = 800
scissors_image_rect.y = 100

running = True

# Loop to continuously receive user input
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        # Handle quit event
        if event.type == pg.QUIT:
            running = False
        
        # Handle mouseclicks
        if event.type == pg.MOUSEBUTTONUP:
            
            # Get position of mouseclicks
            mouse_coords = pg.mouse.get_pos()
            
            # Check which image is clicked and compare with computer's choice
            if rock_image_rect.collidepoint(mouse_coords):
                compare("Rock")
            elif paper_image_rect.collidepoint(mouse_coords):
                compare("Paper")
            elif scissors_image_rect.collidepoint(mouse_coords):
                compare("Scissors")
            else:
                print("you didn't click on anything...")
  

    # Blit the images onto the display surface
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)

    # Update the entire screen
    pg.display.flip()

# Quit program
pg.quit()