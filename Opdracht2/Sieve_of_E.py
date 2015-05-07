import time
import sys

N = int(sys.argv[1])

T1=time.perf_counter()

t=[]
for i in range(2,N):
    t += [i]
    
for k in t:
    if k!=0:
        for l in range(2,int(N/k)+1):
            if 0<k*l<N:
                t[k*l-2]=0

u=[]
for j in t:
    if j!=0:
        u.append(str(j))
    
T2=time.perf_counter()

print('Found', len(u), 'Prime numbers smaller than', N, 'in', T2-T1, 'sec.')

verzetten = open(sys.argv[2], 'w')

for k in range(0,len(u)):
    verzetten.write(u[k] + '\n')