import pygame
import sys

# Setup 
WIDTH, HEIGHT = 500, 500

pygame.init()
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Klikk og dra 2")
clock= pygame.time.Clock()
gui_font= pygame.font.Font(None,30)

BLACK = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)

# Classes

class Square():
    def __init__(self, width, height, pos, color):
        self.rect = pygame.Rect(pos, (width, height))
        self.color= color
        self.pressed = False
        self.moveable =  False

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.check_click()
        
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:          
                    self.moveable = not self.moveable
                    print (f"Status: {self.moveable}")                                  
                    self.pressed = False 
                    return self.moveable   
        
# Functions

# handle box movement
def move_box(box, moveable):
    if moveable:
        box.rect.center = pygame.mouse.get_pos()



# Main loop ::::::::::::::::::::::::::::::::::::::::::::::::::::
firkantliste=[]
for i in range(5):
    firkantliste.append(Square(50, 50, (10, 30+(50*i)), RED))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    
    for i in range(5):
        move_box(firkantliste[i], firkantliste[i].moveable)
        firkantliste[i].draw()

    
    pygame.display.update()
    clock.tick(60)


