
class Set:
    def __init__(self, list1):
        self.elements = {}
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
        for i in self:
            if not(set2.isin(i)):
                return False
        return True

    def isin(self,element):
        for i in self:
            if element == i:
                return True
        return False
    
    def element(self):
        return list(self.elements.keys())

    def __sub__(self, other):
        long = []
        for i in self:
            if other.isin(i):
                #print(i,other.isin(i))
                long.append(i)
        return Set(long)
    
    def __truediv__(self, other):
        long = []
        for i in self:
            if not(other.isin(i)):
                long.append(i)
        return Set(long)

    def __add__(self, set2):
        return Set(self.element() + set2.element())
    
    def __mul__(self, other):
        list1 = []
        for i in self:
            for n in other:
                list1.append((i,n))
        return Set(list1)
    
    def __eq__(self, value):
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





    def power_set(self):
        list1 = self._itterfor(len(self))

        for i in range(len(list1)): #makes sure that we do not have elements like [1,1,1,1,...,1]
            is_the_same = True
            for n in list1[i]:
                if n != list1[i][0]:
                    is_the_same = False
            if is_the_same:
                list1.pop(i)
        return list1



            

class SC(Set):
    def __init__(self, iterable):
        super().__init__(iterable)
        for i in self:
            if type(i) != Set:
                raise TypeError("Invalid agruments: One of the arguments was not a set.")
        Is_valid = []
        for i in self:
            Is_valid.append(False)
        for i in self:
            if not(i.issubsetof(self)):
                raise TypeError(f"Invalid arguments: The element {i} is not a subset of a")
    

        
    def __str__(self):
        return super().__str__() 
    def __iter__(self):
        return super().__iter__()   
    def __len__(self):
        return super().__len__()

            


g = Set([1,2,2,3])
f = Set([1,3,4])
h = Set([Set([1]),Set([2])])
print(g.power_set())

