
import random

import pygame
from the_snake import Snake
from grid import Grid


class Game():
    def __init__(self):
        self.grid = Grid(40,40,20)
        self.snake = Snake()
        self.food = self.drop_food()

        self.score = 1
        
        self.playing = True

    def check_location(self):
        tail = self.snake.body[-1]
        head = self.snake.body[0]
        if head == self.food:
            self.food = self.drop_food()
            self.score +=1
            self.snake.body.append(tail)

        for i in range(1,len(self.snake.body)):
            if self.snake.body[0] == self.snake.body[i] and len(self.snake.body) > 2:
                self.end_game()
        if head[0] < 0 or head[0] > self.grid.num_cols * self.grid.square_size or head[1]< 0 or head[1] > self.grid.num_rows *self.grid.square_size:
            self.end_game()

    def end_game(self):
        self.playing = False
        print(self.score)
                        

    def draw(self,screen):
        food = pygame.Rect(self.food[0],self.food[1],self.grid.square_size,self.grid.square_size)
        self.grid.draw(screen)
        pygame.draw.rect(screen,"yellow",food)
        self.snake.draw(screen)

    def drop_food(self):
        row = random.choice(range(self.grid.num_rows)) *self.grid.square_size
        col = random.choice(range(self.grid.num_cols)) *self.grid.square_size

        return [row,col]
    
        