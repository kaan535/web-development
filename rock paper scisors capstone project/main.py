import pygame
import random

pygame.init()
WIDTH, HEIGHT= 600, 400
FPS = 30
WHITE= 255,255,255
BLACK=0,0,0
FONTSIZE=36

screen=pygame.displayset_mode((WIDTH, HEIGHT))
pygame.displayset_caption("rock paper scissors")
font=pygame.font.Font(none, FONTSIZE)
choices=("rock","paper","scissors")

def get_winner(player, computer):
        if player == computer:
            return "its a Tie!"
        elif (player == "rock" and computer == "scisors") or / (player == "paper" and computer == "rock") or / (player == "rock" and computer == "scissors"):
              return "you win!"
        else:
              return "you lose!"
        