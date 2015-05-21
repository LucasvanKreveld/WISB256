def findRoot(f,a,b,epsilon):
    
    if f(a)>=0 and f(b)>=0:
        print('Check different interval')
        exit()
    
    elif f(a)<=0 and f(b)<=0:
        print('Check different interval')
        exit()
    
    while abs(a-b)>epsilon:
        
        if f(a)==0:
            return(a)
        
        elif f(b)==0:
            return(b)
        
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
    return((a+b)/2)


