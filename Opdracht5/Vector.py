import math

class Vector(object):
    """Geeft een punt in een meerdimensionale ruimte weer.
    
    attributes: dimensie
    """
    
    def __init__(self,n,element=[0]):
        if element==[0]:
            self.element=n*[0]
        elif type(element)==float or type(element)==int:
            self.element=n*[element]
        else:
            self.element=element

    def __str__(self):
        n=len(self.element)
        t=[]
        for i in range(0,n):
            a=str("{0:.6f}".format(self.element[i]))
            t.append(a)
        c=''
        for i in range(0,n):
            c=c+t[i]+'\n'
        return(c)
            
    def lincomb(self,other,alpha,beta):
        n=len(self.element)
        new=[]
        for i in range(0,n):
            w=self.element[i]=alpha*self.element[i]+beta*other.element[i]
            new.append(w)
        return(Vector(n,new))
        
    def scalar(self,alpha):
        n=len(self.element)
        new=[]
        for i in range(0,n):
            w=self.element[i]=alpha*self.element[i]
            new.append(w)
        return(Vector(n,new))
        
    def inner(self,other):
        n=len(self.element)
        value=0
        for i in range(0,n):
            value+=self.element[i]*other.element[i]
        return(value)
    
    def norm(self):
        n=len(self.element)
        square=0
        for i in range(0,n):
            square+=self.element[i]**2
        value=math.sqrt(square)
        return(value)