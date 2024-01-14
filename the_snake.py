import pygame

class Snake():
    def __init__(self,starting_loc,color):
        self.square_size = 20
        self.body_color = color

        self.offset = (10,10)
        
        self.direction = "none"
        self.alive = True

        self.body = [starting_loc]

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

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def crashed(self, num_cols,num_rows,enemy_squares):
        head = self.body[0]

        #death by player
        for square in enemy_squares:
            if head == square:
                return True
        # suiide
        for i in range(1,len(self.body)):
            if head[0] == self.body[i] and len(self.body) > 2:
                return True
            
        #death by falling
        if head[0] < 0 or head[1]< 0 or head[0] > (num_cols-1) * self.square_size or head[1] > (num_rows-1) *self.square_size:
            return True
        

        return False
    
    def draw(self,screen):
        for cell in self.body:
            rect = pygame.Rect(cell[0],cell[1],self.square_size,self.square_size)
            pygame.draw.rect(screen,self.body_color, rect)