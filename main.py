import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((820,820))
title_font = pygame.font.Font(None,40)
game_over_surface = title_font.render("GAME OVER", True, "red")

screen_rect = pygame.Rect(0,0,820,820)

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
            if event.key == pygame.K_RIGHT and game.right_player.direction != "left":
                game.right_player.direction = "right"
            if event.key == pygame.K_LEFT and game.right_player.direction != "right":
                game.right_player.direction = "left"
            if event.key == pygame.K_DOWN and game.right_player.direction != "up":
                game.right_player.direction = "down"
            if event.key == pygame.K_UP and game.right_player.direction != "down":
                game.right_player.direction = "up" 

            if event.key == pygame.K_d and game.left_player.direction != "left":
                game.left_player.direction = "right"
            if event.key == pygame.K_a and game.left_player.direction != "right":
                game.left_player.direction = "left"
            if event.key == pygame.K_s and game.left_player.direction != "up":
                game.left_player.direction = "down"
            if event.key == pygame.K_w and game.left_player.direction != "down":
                game.left_player.direction = "up" 

             
        if event.type == GAME_UPDATE and game.playing:
            game.food.change_color()
            game.right_player.move()
            game.left_player.move()
            game.check_location()
        


    screen.fill('white')
    game.draw(screen)
             
    if game.playing == False:
        # pygame.draw.rect(screen,"black",screen_rect,0,0)
        end_game_data = game.end_game()
        outcome = title_font.render(end_game_data["response"], True, end_game_data["color"])
        # screen.blit(outcome,(320,450,50,50))
        screen.blit(game_over_surface,(320,350,50,50))

        screen.blit(outcome,outcome.get_rect(centerx = screen_rect.centerx,
        centery = screen_rect.centery))
   
    pygame.display.update()
    clock.tick(60)