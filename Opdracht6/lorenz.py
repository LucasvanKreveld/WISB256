from scipy.integrate import odeint
    


class Lorenz(object):

    """bla bla bla
    nog meer bla"""

    def __init__(self,punt,sigma,rho,beta):
        self.punt=punt
        self.sigma=sigma
        self.rho=rho
        self.beta=beta
        
    def f(self,xyz,t):
        [x,y,z] = xyz 
        f = [self.sigma*(y - x), x*(self.rho - z) - y, x*y - self.beta*z]
        return f

    def __str__(self):
        return str(self.punt)

    def solve(self,T,dt):
        tijdstappen=[]
        t=0
        while t<T:
            tijdstappen.append(t)
            t += dt
        return odeint(self.f,self.punt,tijdstappen)
        
        
        
    