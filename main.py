import pygame
import sys
from game import Game

screen = pygame.display.set_mode((800,800))

game = Game()

clock = pygame.time.Clock()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and game.snake.direction != "left":
                game.snake.direction = "right"
            if event.key == pygame.K_LEFT and game.snake.direction != "right":
                game.snake.direction = "left"
            if event.key == pygame.K_DOWN and game.snake.direction != "up":
                game.snake.direction = "down"
            if event.key == pygame.K_UP and game.snake.direction != "down":
                game.snake.direction = "up" 

            if event.key == pygame.K_d and game.player1.direction != "left":
                game.player1.direction = "right"
            if event.key == pygame.K_a and game.player1.direction != "right":
                game.player1.direction = "left"
            if event.key == pygame.K_s and game.player1.direction != "up":
                game.player1.direction = "down"
            if event.key == pygame.K_w and game.player1.direction != "down":
                game.player1.direction = "up" 

             
        if event.type == GAME_UPDATE and game.playing:
            game.snake.move()
            game.player1.move()
            game.check_location()
                 
    screen.fill('white')
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)