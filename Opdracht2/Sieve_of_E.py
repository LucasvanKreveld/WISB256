import time
import sys

N = int(sys.argv[1])

T1=time.perf_counter()

t=[]
for i in range(2,N):
    t += [str(i)]
    
for p in range(2,N):
    x = True
    for m in range(2,int(p/2+1)):
        if x == True and p%m==0:
            t.remove(str(p))
            x = False       #om p niet meerdere malen te verwijderen

T2=time.perf_counter()

print('Found', len(t), 'Prime numbers smaller than', N, 'in', T2-T1, 'sec.')

verzetten = open(sys.argv[2], 'w')

for k in range(0,len(t)):
    verzetten.write(t[k] + '\n')