import random

import pygame
from the_snake import Snake
from grid import Grid


class Game():
    def __init__(self):
        self.grid = Grid(40,40,20)
        self.snake = Snake([20,20],"black")
        self.player1 = Snake([600,600],"blue")
        self.food = self.drop_food()

        self.score = 1
        
        self.playing = True

    def check_location(self):

        if self.snake.body[0] == self.food:
            tail = self.snake.body[-1]
            self.food = self.drop_food()
            self.snake.body.append(tail)

        if self.player1.body[0] == self.food:
            tail = self.player1.body[-1]
            self.food = self.drop_food()
            self.player1.body.append(tail)

        if self.snake.crashed(self.grid.num_cols,self.grid.num_rows,self.player1.body) == True:
            print("Snake died, Player1 wins")
            self.end_game()
        if self.player1.crashed(self.grid.num_cols,self.grid.num_rows,self.snake.body) == True:
            print("Player1 died, Snake wins")
            self.end_game()
    def end_game(self):
        self.playing = False
        print(f"player1: {len(self.player1.body)}")
        print(f"snake: {len(self.snake.body)}")

        if self.player1.body[0] == self.snake.body[0]:
            print("TIE")
        
                        

    def draw(self,screen):
        food = pygame.Rect(self.food[0],self.food[1],self.grid.square_size,self.grid.square_size)
        self.grid.draw(screen)
        pygame.draw.rect(screen,"brown",food)
        self.snake.draw(screen)
        self.player1.draw(screen)

    def drop_food(self):
        row = random.choice(range(self.grid.num_rows)) *self.grid.square_size
        col = random.choice(range(self.grid.num_cols)) *self.grid.square_size

        return [row,col]
    
        