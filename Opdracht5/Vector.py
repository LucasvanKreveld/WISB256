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
            a=str(self.element[i])
            t.append(a)
        c=''
        for i in range(0,n-1):
            c=c+t[i]+'\n'
        c=c+t[n-1]
        return(c)
            
    def lincomb(self,other,alpha,beta):
        n=len(self.element)
        new=[]
        for i in range(0,n):
            w=alpha*self.element[i]+beta*other.element[i]
            new.append(w)
        return(Vector(n,new))
        
    def scalar(self,alpha):
        n=len(self.element)
        new=[]
        for i in range(0,n):
            w=alpha*self.element[i]
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
    
    def Proj(self,u):
        x = self.inner(u)/u.inner(u)
        y = u.scalar(x)
        return(y)

def GrammSchmidt(V):
    n=len(V[0].element)
    m=len(V)
    U=m*[0]
    for k in range(0,m):
        y=Vector(n)
        for l in range(0,k):
            y.lincomb(V[k].Proj(U[l]),1,1)
        U[k]=V[k].lincomb(y,1,-1)
    for j in range(0,m):
        U[j]=U[j].scalar(1/U[j].norm())
    return(U)