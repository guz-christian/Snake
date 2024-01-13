import pygame

class Snake():
    def __init__(self):
        self.body = [[0,0]]
        self.head = [0,0]
        self.tail = []

        self.direction = "none"

        self.square_size = 20

    def move(self):
        head = self.body[0]
        if self.direction != "none":
            self.body.pop()
        if self.direction == "right":
            self.body.insert(0,[head[0] + self.square_size, head[1]])

        if self.direction == "left":
            self.body.insert(0,[head[0] - self.square_size, head[1]])
        
        if self.direction == "down":
            self.body.insert(0,[head[0], head[1] + self.square_size])

        if self.direction == "up":
            self.body.insert(0,[head[0], head[1] - self.square_size])


    def draw(self,screen):
        for cell in self.body:
            rect = pygame.Rect(cell[0],cell[1],self.square_size,self.square_size)
            pygame.draw.rect(screen,"black", rect)