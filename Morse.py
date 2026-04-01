import pygame
import sys
import random
from Simplitial_Complises import *

def MEthod1_step(self: SC, prev_dic = {}) -> list[list[Set],dict] :
    new = SC(SimC.Simplisial_Collaps())
    if len(self) != 1:
        if len(self) != len(new):
            return [new.element(),prev_dic]
        try:
            prev_dic[new.highest_dim] += 1
        except:
            prev_dic[new.highest_dim] = 1
        return [self.RemoverHighcomplex(),prev_dic]
    else:
        return self
    
def draw(selfit, draw_points = False, debbug = False):
    try:
        for i in selfit.dim_simpl[2]:
            n = selfit.border(i)
            h = {}
            j =[]
            for i in n:
                h[selfit.border(i)[0]] = 1
                h[selfit.border(i)[1]] = 1
            for i in h:
                j.append(i)
            pygame.draw.polygon(screen,(0,0,255),[selfit.cords[j[0]],selfit.cords[j[1]],selfit.cords[j[2]]])
    except: 
        if debbug: print("Error, cannot print point of dim 2")
    try:
        for i in selfit.dim_simpl[1]:
            n = selfit.border(i)
            pygame.draw.line(screen,(0,255,0),selfit.cords[n[0]],selfit.cords[n[1]],3)
    except: 
        if debbug:  print("Error, cannot print point of dim 1")
    try:
        for i in selfit.dim_simpl[0]:
            if draw_points:
                pygame.draw.circle(screen,(255,0,0),selfit.cords[i],5)
            text_surface = font.render(str(i), True, (0,0,0))
            text_render = text_surface.get_rect(center = selfit.cords[i])
            screen.blit(text_surface, text_render)
    except: 
        if debbug:  print("Error, cannot print point of dim 0")    

  

pygame.init()
pygame.font.init()
screen_width = 800
screen_height = 800
center =(screen_width/2,screen_height/2)
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("newtimesroman",30)

SimC = SC([Set(["good"]),Set([2]),Set(["good",2]),Set([4]),Set([3,2]),Set([3,2,4]),Set(["good",4]),Set([4,2]),Set([3]),Set([5]),Set([5,3]),Set([3,4])])
SimC.findNoOfCrit_Meth1()
SimC.Define_graphical_cords(False)



    
no_of_crit = {}
index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))

    if len(SimC) != 2 and index == 100:
        SimC = SC(MEthod1_step(SimC,no_of_crit)[0])
        SimC.Define_graphical_cords(False)
        draw(SimC)
        index = 0
    else:
        draw(SimC)
        index += 1

    pygame.display.flip()
    pygame.time.wait(1)

pygame.quit()
