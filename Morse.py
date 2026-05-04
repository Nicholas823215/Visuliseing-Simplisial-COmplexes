import pygame
import sys
from Simplitial_Complises import *

def MEthod1_step(self: SC, prev_dic = {}) -> list[list[Set],dict] :
    new = SC(SimC.Simplisial_Collaps())
    if len(self) != 2:
        if self != new:
            return [new.element(),prev_dic]
        try:
            prev_dic[self.highest_dim] += 1
        except:
            prev_dic[self.highest_dim] = 1
        return [self.RemoverHighcomplex(),prev_dic]
    else:
        return [self, prev_dic]
    
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

'''SimC = SC([Set([1]),Set([2]),Set([3]),Set([4]),Set([5]),
               Set([1,2]),Set([1,5]),Set([2,4]),Set([2,5]),Set([5,4]),Set([1,4]),Set([1,3]),Set([3,4]),Set([2,3]),
               Set([1,2,5]),Set([5,2,4]),Set([2,4,3]),Set([1,3,4]),
               Set([6]),Set([7]),Set([8]),Set([9]),Set([10]),Set([11]),
               Set([9,6]),Set([9,7]),Set([9,10]),Set([9,11]),Set([9,3]),Set([3,11]),Set([3,8]),Set([3,6]),Set([6,7]),Set([6,8]),Set([7,8]),Set([7,10]),Set([10,8]),Set([10,11]),Set([11,8]),
               Set([6,9,7]),Set([9,7,10]),Set([10,7,8]),Set([10,11,8]),Set([6,3,8]),Set([3,11,8]),Set([3,9,11]),
               Set([4,8,7]),Set([4,5,7]),Set([5,7,6]),Set([5,1,6]),Set([1,6,8]),Set([1,4,8]),
               Set([2,1,6]),Set([2,9,6]),Set([2,3,9]),Set([1,6,3]),
               Set([12]),Set([13]),Set([14]),Set([15]),Set([16]),
               Set([12,16]),Set([12,14]),Set([12,15]),Set([12,13]),Set([16,15]),Set([13,15]),Set([13,14]),Set([14,15]),Set([14,16]),
               Set([12,14,16]),Set([14,15,16]),Set([13,14,15]),Set([12,13,15])])'''
SimC = SC([Set([1]),Set([2]),Set([3]),Set([4]),Set([5]),Set([6]),
          Set([1,2]),Set([2,3]),Set([3,4]),Set([4,2]),Set([1,5]),Set([5,6]),Set([6,1])])







#SimC = SC([Set(["good"]),Set([2]),Set(["good",2]),Set([4]),Set([3,2]),Set([3,2,4]),Set(["good",4]),Set([4,2]),Set([3]),Set([5]),Set([5,3]),Set([3,4])])
SimC.findNoOfCrit_Meth1()
SimC.Define_graphical_cords(False)



    
no_of_crit = {}
index = 0
fin = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))

    if len(SimC) != 2 and index == 100:
        hi = MEthod1_step(SimC,no_of_crit)
        SimC = SC(hi[0])
        no_of_crit = hi[1]
        SimC.Define_graphical_cords(False)
        draw(SimC)
        index = 0
    else:
        if len(SimC) <= 2 and fin == False:
            try:
                no_of_crit[0] += 1
            except:
                no_of_crit[0] = 1
            fin = True
        draw(SimC)
        index += 1
    te = {}
    for i in no_of_crit.items():
        te[f"# of crit of index {i[0]}"] = i[1]
    sti = ""
    for i in te.items():
        sti += i[0]+" :"+ str(i[1])+ ", "
    sti = sti[:-2]
    text_surface = font.render(sti, True, (0,0,0))
    text_render = text_surface.get_rect(center = (400,100))
    screen.blit(text_surface, text_render)
    pygame.display.flip()
    pygame.time.wait(1)

pygame.quit()
