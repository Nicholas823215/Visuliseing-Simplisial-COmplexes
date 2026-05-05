import random
import math
import time

class Set:
    def __init__(self, list1 = []):
        self.elements = {}
        if list1 != []:
            try:
                list1.__iter__()
            except:
                raise TypeError(f"{list1} is NOT an itterable type")
            for i in list1:
                self.elements[i] = 1

    def __str__(self):
        return str(list(self.elements.keys()))
    def __iter__(self):
        return list(self.elements.keys()).__iter__()
    def __len__(self):
        return len(self.element())

    def issubsetof (self, set2):
        if self.__len__() == 0:
            return True
        for i in self:
            if not(set2.isin(i)):
                return False
        return True
    
    def issupersetof(self, set2):
        if set2.__len__() == 0:
            return False
        for i in set2:
            if not(self.isin(i)):
                return False
        return True

    def isin(self,element):
        if self.__len__() == 0:
            return False
        for i in self:
            if element == i:
                return True
        return False
    
    def element(self):
        return list(self.elements.keys())
    
    def add(self, element):
        self.elements[element] = 1


    def __sub__(self, other):
        if self.__len__() == 0:
            return Set()
        long = []
        for i in self:
            if other.isin(i):
                #print(i,other.isin(i))
                long.append(i)
        return Set(long)
    
    def __truediv__(self, other):
        if self.__len__() == 0:
            return Set()
        long = []
        for i in self:
            if not(other.isin(i)):
                long.append(i)
        return Set(long)

    def __add__(self, set2):
        if self.__len__() == 0:
            return set2
        return Set(self.element() + set2.element())
    
    def __mul__(self, other):
        if self.__len__() == 0:
            return Set()
        list1 = []
        for i in self:
            for n in other:
                list1.append((i,n))
        return Set(list1)
    
    def __eq__(self, value):
        if self.__len__() == 0 and value.__len__() == 0:
            return True
        elif self.__len__() == 0:
            return False
        elif value.__len__() == 0:
            return False
        for i in self:
            if not(value.isin(i)):
                return False
        for i in value:
            if not(self.isin(i)):
                return False
        return True

    def __hash__(self):
        return(hash(tuple(self.element())))
    
    def __and__(self, other):
        return self.__sub__(other)
    
    def __or__(self, value):
        return self.__add__(value)
    
    def _itterfor (self, n, list1 =[]): #redo this
        if n != 0:
            for i in self:
                list1 += self._itterfor(n-1,)
        else:
            for i in self:
                list1.append([i])
            return list1

    '''def power_set(self):
        list1 = self._itterfor(len(self))

        for i in range(len(list1)): #makes sure that we do not have elements like [1,1,1,1,...,1]
            is_the_same = True
            for n in list1[i]:
                if n != list1[i][0]:
                    is_the_same = False
            if is_the_same:
                list1.pop(i)
        return list1'''



            

class SC(Set):
    def __init__(self, iterable):
        self.No_crit_Meth1 = {}
        super().__init__(iterable)
        self.add(Set())
        for i in self:
            if type(i) != Set:
                raise TypeError("Invalid agruments: One of the arguments was not a set.")
        self.dim_simpl = {}
        for i in self:
            try:
                self.dim_simpl[len(i)-1].append(i)
            except KeyError:
                self.dim_simpl[len(i)-1] = [i]
        self.highest_dim  = 0
        while self._IsIn(self.highest_dim):
            self.highest_dim += 1
        self.highest_dim -= 1
        
    def _IsIn(self,x):
        try:
            self.dim_simpl[x]
            return True
        except KeyError:
            return False
    
    def border(self, set2: Set):
        list1 = []
        if not(self.isin(set2)):
            return None
        else:
            for i in self.dim_simpl[len(set2)-2]:
                if i.issubsetof(set2):
                    list1.append(i)
        return list1

    def Define_graphical_cords(self,random1 = True, r = (100,101), debbug = False):
        self.cords = {}
        if random1:
            self.cords[self.dim_simpl[0][0]] = [random.randint(200,500),random.randint(400,600)]
        else:
            self.cords[self.dim_simpl[0][0]] = [400,400]
        h1 = self.cords[self.dim_simpl[0][0]]
        try:
            if random1:
                angle = random.randint(361,581)/100
            else:
                angle = 3.92
            '''for some reason when the angles where smalller or larger then this range it gave a bad display'''
            if debbug: print(angle)
            vectpr_angle = [math.cos(angle),math.sin(angle)]
            self.cords[self.dim_simpl[0][1]] = [100*vectpr_angle[0]+h1[0],100*vectpr_angle[1]+h1[1]]
            h2 = self.cords[self.dim_simpl[0][1]]
        except:
            return None
        n = len(self.dim_simpl[0])
        for i in self.dim_simpl[0]:
            if debbug: print(i)
        for i in range(2,len(self.dim_simpl[0])):
            if debbug: print(self.dim_simpl[0][i-2])
            mif_point = [(h1[0] + h2[0])/2 , (h1[1] + h2[1])/2]
            vector1 = [pow(-1,i)*r[0]/pow(pow((h1[1]-h2[1])/(h1[0]-h2[0]),2)+1,1/2)*(-(h1[1]-h2[1])/(h1[0]-h2[0])) , pow(-1,i)*r[0]/pow(pow((h1[1]-h2[1])/(h1[0]-h2[0]),2)+1,1/2)]
            for n in range(2):
                mif_point[n] += vector1[n]
            self.cords[self.dim_simpl[0][i]] = mif_point
            h1 = h2
            h2 = self.cords[self.dim_simpl[0][i]]
            if debbug: print(self.dim_simpl[0][i],h1,h2)

    def Simplisial_Collaps(self,debugging = False) -> list[Set]: #-> SC with one simplitial chollaps performed
        
        final = []
        if len(self) == 2:
            for i in self:
                final.append(i)
            if debugging:
                print("Same as before, only one point")
            return final
        for i in self.dim_simpl[self.highest_dim]:
            if debugging:
                print("set1:            ",i)
            remove = []
            nmin1simp = self.border(i)
            for n in nmin1simp:
                is_valid = True
                if debugging:
                    print("element of set1: ",n)
                for h in self.dim_simpl[self.highest_dim]:
                    if debugging:
                        print("against:         ",h)
                    if n in self.border(h) and n != [] and h != i:
                        is_valid = False
                        if debugging:
                            print("                  Fail!!!")
                    if not(is_valid):
                        break
                if not(is_valid):
                    pass
                else:
                    remove = [n,i]
                if remove != []:
                    break
            if remove != []:
                break
        if debugging:
            print(final)
        for i in self.element():
            if not(i in remove):
                final.append(i)
        if debugging:
            for i in final:
                print(str(i)+", ",end="")
            print()
        if self == Set(final):
            if debugging:
                print("Same as before")
        else:
            if debugging:
                print("Reduced")
        return final

    def RemoverHighcomplex(self, debugging = False):
        for i in self.dim_simpl[self.highest_dim]:
            if debugging:
                print("set1:            ",i)
            return (self/Set([i])).element() 
        
    def findNoOfCrit_Meth1(self, debbug = False):
        SimC = [self,SC([Set([])])]
        while len(SimC[0]) != 1:
            while len(SimC[0]) != len(SimC[1]):
                if debbug:
                    print("Before Reduction:")
                    print("SimC[0] = {",end="")
                    for i in SimC[0]:
                        print(i,", ",end="")
                    print("}")
                    print("SimC[1] = {",end="")
                    for i in SimC[1]:
                        print(i,", ",end="")
                    print("}")
                    print()
                SimC[1] = SimC[0]
                SimC[0] = SC(SimC[0].Simplisial_Collaps())
                if debbug:
                    print("After Reduction:")
                    print("SimC[0] = {",end="")
                    for i in SimC[0]:
                        print(i,", ",end="")
                    print("}")
                    print("SimC[1] = {",end="")
                    for i in SimC[1]:
                        print(i,", ",end="")
                    print("}")
                    print()
            try:
                self.No_crit_Meth1[SimC[0].highest_dim] += 1
            except:
                self.No_crit_Meth1[SimC[0].highest_dim] = 1
            SimC[0] = SC(SimC[0].RemoverHighcomplex())
            if debbug:
                print("REMOVED COMPLEX")
                print("SimC[0] = {",end="")
                for i in SimC[0]:
                    print(i,", ",end="")
                print("}")
                print("SimC[1] = {",end="")
                for i in SimC[1]:
                    print(i,", ",end="")
                print("}")
                print()
            



            






    def __str__(self):
        elemts = []
        for i in self.elements:
            t = []
            for n in i.elements:
                t.append(n)
            elemts.append(t)
        return str(elemts)
    def __iter__(self):
        return super().__iter__()   
    def __len__(self):
        return super().__len__()

            

if __name__ == "__main__":
    g = Set([1,2,2,3])
    f = Set()
    h = SC([Set([1]),Set([2]),Set([1,2]),Set([3]),Set([3,2]),Set([1,3]),Set([1,2,3]),Set([1,4]),Set([4,2])])


    print(h.border(Set([1,4]))[0])
