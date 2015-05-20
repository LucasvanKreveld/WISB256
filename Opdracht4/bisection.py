def findRoot(f,a,b,epsilon):
    
    if f(a)>=0 and f(b)>=0:
        print('Check different interval')
        exit()
    
    elif f(a)<=0 and f(b)<=0:
        print('Check different interval')
        exit()
    
    while abs(a-b)>=epsilon:
        
        if f(a)==0:
            print('x =', a)
            exit()
        
        elif f(b)==0:
            print('x =', b)
            exit()
        
        elif f(a)<0 and f(b)>0:
            if f((a+b)/2)<0:
                a = (a+b)/2
            else:
                b = (a+b)/2
    
        else:
            if f((a+b)/2)<0:
                b = (a+b)/2
            else:
                a = (a+b)/2
    print((a+b)/2)
        

