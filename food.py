import pygame


class Food():
    def __init__(self,location) -> None:
        self.location = location
        self.colors = ['red','orange','yellow','green','blue','purple']
        self.color_index = 0

    def change_loc(self,new_loc):
        self.location = new_loc

    def change_color(self):
        self.color_index +=1
        if self.color_index == len(self.colors):
            self.color_index = 0

    def draw(self,screen,square_size):
        food_rect = pygame.Rect(self.location[0],self.location[1],square_size,square_size)
        pygame.draw.rect(screen,self.colors[self.color_index],food_rect)