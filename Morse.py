import pygame
import sys
import random
from Simplitial_Complises import *

pygame.init()
pygame.font.init()
screen_width = 800
screen_height = 800
center =(screen_width/2,screen_height/2)
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("newtimesroman",30)

SimC = SC([Set(["good"]),Set([2]),Set(["good",2]),Set([4]),Set([3,2]),Set([3,2,4]),Set(["good",4]),Set([4,2]),Set([3]),Set([5]),Set([5,3]),Set([3,4])])

SimC = SC(SimC.Simplisial_Collaps())
SimC = SC(SimC.Simplisial_Collaps())
SimC = SC(SimC.Simplisial_Collaps())
SimC = SC(SimC.Simplisial_Collaps())
SimC = SC(SimC.Simplisial_Collaps())
SimC.Define_graphical_cords()

print(SimC.highest_dim)
def draw(draw_points = False):
    try:
        for i in SimC.dim_simpl[2]:
            n = SimC.border(i)
            h = {}
            j =[]
            for i in n:
                h[SimC.border(i)[0]] = 1
                h[SimC.border(i)[1]] = 1
            for i in h:
                j.append(i)
            pygame.draw.polygon(screen,(0,0,255),[SimC.cords[j[0]],SimC.cords[j[1]],SimC.cords[j[2]]])
    except: pass
    try:
        for i in SimC.dim_simpl[1]:
            n = SimC.border(i)
            pygame.draw.line(screen,(0,255,0),SimC.cords[n[0]],SimC.cords[n[1]],3)
    except: pass
    try:
        for i in SimC.dim_simpl[0]:
            if draw_points:
                pygame.draw.circle(screen,(255,0,0),SimC.cords[i],5)
            text_surface = font.render(str(i), True, (0,0,0))
            text_render = text_surface.get_rect(center = SimC.cords[i])
            screen.blit(text_surface, text_render)
    except: pass

    
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))

    draw()

    pygame.display.flip()
    pygame.time.wait(1)

pygame.quit()
