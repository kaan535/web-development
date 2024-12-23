import pygame
import random

pygame.init()
WIDTH, HEIGHT= 600, 400
FPS = 30
WHITE= 255,255,255
BLACK=0,0,0
FONTSIZE=36

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rock paper scissors")
font=pygame.font.Font(None, FONTSIZE)
choices=("rock","paper","scissors")

def get_winner(player, computer):
        if player == computer:
            return "its a Tie!"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
                   (player == "rock" and computer == "scissors"):
              return "you win!"
        else:
              return "you lose!"

def main():
      running = True
      player_choice = None
      computer_choice = None
      result = ""

      while running:
            for event in pygame.event.get():
                  if event.type==pygame.QUIT:
                        running = False
                  if event.type==pygame.keydown:
                        if event.key == pygame.K_r:
                              player_choice = "rock"
                        elif event.key == pygame.K_p:
                              player_choice = "paper"
                        elif event.key == pygame.K_s:
                              player_choice = "scissors"
                        if player_choice:
                              computer_choice = random.choice(choices)
                              result = get_winner

                        screen.fill(WHITE)
                        
                        if player_choice:
                              player_text = font.render(f"you chose: {player_choice}")
                              computer_text = font.render(f"you chose: {computer_choice}")
                              result_text = font.render(result)

                              screen.blit(player_text,(50,50))
                              screen.blit(computer_text,(50,100))
                              screen.blit(player_text,(50,150))
                        pygame.display.flip()
                        pygame.time.clock().tick(FPS)
      pygame.quit()
if __name__ ==" __main__":
      main()