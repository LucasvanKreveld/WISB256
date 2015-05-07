import random
import math
import sys

if len(sys.argv)==1:
    print('Use: estimate_pi.py N L')
    exit()

if len(sys.argv)==2:
    print('Use: estimate_pi.py N L')
    exit()
    
N = int(sys.argv[1])
L = float(sys.argv[2])

if L<0 or L>1:
    print('AssertionError: L should be smaller than 1')
    exit()
    
if len(sys.argv)==4:
    seed = int(sys.argv[3])
    random.seed(seed)
    
def drop_needle(L):
    count = 0
    for i in range(1, N+1):
        x = random.random()
        a = random.vonmisesvariate(0,0)
        if 0 <= x+L*math.cos(a) <= 1:
            count += 1
        
    probability = 1 - float(count)/float(N)
    estimation = 2*L/probability
        
    print(count, 'hits in', N, 'tries')
    print('Pi =', estimation)
            
drop_needle(L)
        
