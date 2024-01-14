import random

from food import Food
from the_snake import Snake
from grid import Grid


class Game():
    def __init__(self):
        self.grid = Grid(40,40,20)
        self.offset = (10,10)
        self.left_player = Snake(self.random_loc(),"yellow")
        self.right_player = Snake(self.random_loc(),"blue")

        self.food = Food(self.random_loc())

        self.unavailable_locations = []
        
        self.playing = True

    def check_location(self):
        # check for food
        if self.left_player.body[0] == self.food.location:
            self.left_player.grow()
            self.food.change_loc(self.random_loc())

        if self.right_player.body[0] == self.food.location:
            self.right_player.grow()
            self.food.change_loc(self.random_loc())

        #chech if crashed
        if self.left_player.crashed(self.grid.num_cols,self.grid.num_rows,self.right_player.body) == True:
            self.playing = False
            self.left_player.alive = False
        if self.right_player.crashed(self.grid.num_cols,self.grid.num_rows,self.left_player.body) == True:
            self.playing = False
            self.right_player.alive = False

    def end_game(self):
        if self.right_player.body[0] == self.left_player.body[0]:
            return {"response":"TIE","color":"red"}

        if self.right_player.alive == True:
            return {"response":f"{self.right_player.body_color} player wins!","color":self.right_player.body_color}
        if self.left_player.alive == True:
            return {"response":f"{self.left_player.body_color} player wins!","color":self.left_player.body_color}              

    def draw(self,screen):
        self.grid.draw(screen)

        self.food.draw(screen,self.grid.square_size)
        self.left_player.draw(screen)
        self.right_player.draw(screen)

    def random_loc(self):

        row = random.choice(range(self.grid.num_rows)) *self.grid.square_size + self.offset[0]
        col = random.choice(range(self.grid.num_cols)) *self.grid.square_size + self.offset[1]



        return [row,col]
    
        