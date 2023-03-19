# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 640
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
 
def Sun(X,Y):
    pygame.draw.circle(screen,(240, 240, 10),(X,Y),30)#Sun

def Sky(R,G,B):
    screen.fill((R,G,B))

def moon(M,N,S,L,R,G,B):
    pygame.draw.circle(screen,(249, 250, 235),(M,N),30)
    pygame.draw.circle(screen,(R,G,B),(S,L,),25)
    


X=430
Y=100

M=90
N=708

S=100
L=698

R=100
G=182
B=245
# ---------------------------

running = True
while running:
    # EVENT HANDLING

    # GAME STATE UPDATES
    # All game math and comparisons happen here
#Dimensions: X 498  Y 385 
    # DRAWING
    Sky(R,G,B) # always the first drawing command

    pygame.draw.rect(screen, (92, 204, 90),(0,305,498,80))#Grass

    

    
    pygame.draw.rect(screen,(210,100,110),(199,205,100,100))#House
    pygame.draw.polygon(screen, (210,100,110), ((199,205),(299,205),(249,155)))#Roof
    pygame.draw.rect(screen,(188, 194, 79),(209,215,30,30))#windows
    pygame.draw.rect(screen,(188, 194, 79),(259,215,30,30))
    pygame.draw.rect(screen,(87, 66, 20),(235,265,30,40))#Door
    
    Sun(X,Y)
    moon(M,N,S,L,R,G,B)

    
    pygame.draw.rect(screen,(87, 66,20),(79,260,15,45))#Tree
    pygame.draw.polygon(screen, (9, 145, 68),((39,270),(134,270),(86.5,210)))
    pygame.draw.polygon(screen, (9, 145, 68),((45,240),(128,240),(86.5,180)))
    pygame.draw.line(screen,(87, 66, 20),(249,155),(187,217),8)#Roof Outline
    pygame.draw.line(screen,(87, 66, 20),(249,155),(311,217),8)

    if Y >=385 and X>=249:#start of the night
        X-=4
        Y+=4
        
        M+=4
        N-=4
        S+=4
        L-=4
        
        R=11
        G=69
        B=140
        
    if Y>=385 and X<249:#end of the night 
        X-=4
        Y-=4
        
        M+=4
        N+=4
        S+=4
        L+=4
        
        R=9
        G=58
        B=117
        
        
        
    if Y<385 and X<249 :#afternoon
        X+=4
        Y-=4
        
        M-=4
        N+=4
        S-=4
        L+=4
        
        R=33
        G=105
        B=194
        
    if Y<385 and X>=249:#morning
        X+=4
        Y+=4
        
        M-=4
        N-=4
        S-=4
        L-=4

        R=100
        G=182
        B=245
        
    
    

   
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
