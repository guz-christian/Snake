import pygame


class Grid():
    def __init__(self,num_rows,num_cols,square_size):
        self.offset = (10,10)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.square_size = square_size
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column],end = " ")
            print()
    
    def draw(self,screen):
         for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_rect = pygame.Rect(column*self.square_size + self.offset[0],row*self.square_size+ self.offset[1],self.square_size -1,self.square_size -1)
                pygame.draw.rect(screen,"gray",cell_rect)