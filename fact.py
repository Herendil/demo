def fact(n):
    res = 1
    for i in range(n):
        res*=(i+1)
    return res

def coefbin(k,n):
    if(k<=n):
        return(fact(n)/(fact(k)*fact(n-k)))
    else:
        return(0)

def new(x,y,n):
    s=0
    for i in range(n+1):
        s+=coefbin(i,n)*(x**k)*(y**(n-k))
    return(s)
