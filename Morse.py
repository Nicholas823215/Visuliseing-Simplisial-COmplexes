import pygame
import sys
import random

pygame.init()
pygame.font.init()
screen_width = 800
screen_height = 600
center =(screen_width/2,screen_height/2)
screen = pygame.display.set_mode((screen_width, screen_height))

class Set:
    elements = {}

    def __init__(self,set1: list,create_Power_set = True):

        for i in self.elements:
            self.elements[i] = True

        if create_Power_set:
            self.CreatePowerSet()

    def CreatePowerSet(self):
        self.PowerSet.append([])
        length = len(self.elements)
        for i in self.elements:
            if not([i] in self.PowerSet):
                self.PowerSet.append([i])
        if length >= 2:
            for i in self.elements:
                for n in self.elements:
                    if n != i and not([n,i] in self.PowerSet or [i,n] in self.PowerSet):
                        self.PowerSet.append([i,n])
        if length >= 3:
            for i in self.elements:
                for n in self.elements:
                    for o in self.elements:
                        Is_alredy_there = [i,n,o] in self.PowerSet or [i,o,n] in self.PowerSet or [n,i,o] in self.PowerSet or [n,o,i] in self.PowerSet or [o,i,n] in self.PowerSet or [o,n,i] in self.PowerSet
                        if n != i and i != o and n != o and not(Is_alredy_there):
                            self.PowerSet.append([i,n,o])

    def IsIn(self, it):
        if self.elements.get(it) == None:
            return False
        return True
    
    def IsSubSet(self, it):
        Is = []
        for i in it.elements:
            Is.append(False)
        
        for i in range(len(it.elements)):
            for n in self.elements:
                if n == it[i]:
                    Is[i] = True
        
        if False in Is:
            return False
        return True
    
    def add(self, i):
        self.elements[i] = 1

    def remove(self, i):
        for n in range(len(self.elements)):
            if i == n:
                self.element.pop(n)      

    PowerSet = []

def Union(set1: Set, set2: Set) -> Set:
    return Set(set1.elements + set2.elements)

def Intsec(set1: Set, set2: Set) -> Set:
    end_list = []
    for i in set1.elements:
        if set2.IsIn(i):
            end_list.append(i)
    return Set(end_list)

class SC:
    def __init__(self,the: list[Set],record_dim_info = True):
        list1 = []
        for i in the:
            list1 += i.PowerSet
        self.elements = Set(list1).elements
        if record_dim_info:
            for i in self.elements:
                if len(i) == 1:
                    self.dim0.append(i)
                if len(i) == 2:
                    self.dim1.append(i)
                if len(i) == 3:
                    self.dim2.append(i)
        
    elements = None
    dim0 = []
    dim1 = []
    dim2 = []

def statistical_funct(boundury1 = int(screen_height/2), boundury2 = int(screen_width/2),spread = 100):
    return [random.randint(boundury1-100,boundury1+100),random.randint(boundury2-100,boundury2+100)]

def Cords_Morse_Function(sc: SC):
    cords = []
    for i in sc.dim0:
        cords.append([statistical_funct(),i])
    return cords

def InverseList(elemnt, list1: list):
    for i in range(len(list1)):
        if list1[i] == elemnt:
            return i
    return None

d = Set([1,2,3])
u = Set([1,2,10])
print(Intsec(d,u).elements)
sc = SC([d,u])
graph = Cords_Morse_Function(sc)
print(Cords_Morse_Function(sc))

def Unpack(lest1):
    final = []
    for i in lest1:
        final += i
    return final

font = pygame.font.SysFont(None,30)
text_surface = []
text_rect = []
for i in graph:
    text_surface.append(font.render(str(i[1]),True,(0,0,0)))
    text_rect.append(text_surface[-1].get_rect())
    text_rect[-1].center = (i[0])

graph0 = Unpack(graph)
graph1 = []
print(graph1)
print(InverseList(2,d.elements))
for i in sc.dim1:
    print(graph0)
    Index1 = InverseList([i[0]],graph0)
    Index2 = InverseList([i[1]],graph0)
    Index1 -= 1
    Index2 -= 1
    graph1.append([graph0[Index1],graph0[Index2]])
print(graph1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))

    for i in range(len(graph)):
        #pygame.draw.circle(screen,(0,0,255),graph[i][0],2)
        screen.blit(text_surface[i], text_rect[i])
    for i in graph1:
        pygame.draw.line(screen,(255,0,0),i[0],i[1],5)

    pygame.display.flip()
    pygame.time.wait(1)

pygame.quit()
