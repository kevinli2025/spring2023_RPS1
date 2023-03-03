# File created by: Kevin Li
 
# import libraries

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 800
HEIGHT = 800
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initialize pygame
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
rock_image_rect.x = 300
rock_image_rect.y = 500

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = 200
paper_image_rect.y = 400

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = 200
scissors_image_rect.y = 200

running = True

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # 
        if event.type == pg.MOUSEBUTTONUP:
            # 
            print(pg.mouse.get_pos()[0])
            # 
            print(pg.mouse.get_pos()[1])
            # 
            mouse_coords = pg.mouse.get_pos()
            # if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            #     print("i clicked the rock")
            # else:
            #     print("no rock....")
            # 
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock..")
            elif paper_image_rect.collidepoint(mouse_coords):
                pass            
            else:
                print("you didn't click on anythin...")
    ########## input ###########
    # HCI - human computer interaction...
    # keyboard, mouse, controller, vr headset
    ########## update ###################
    # rock_image_rect.x += 1
    # rock_image_rect.y += 1

    ############ draw ###################
    screen.fill(BLACK)

    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(rock_image, rock_image_rect)

    pg.display.flip()

pg.quit()