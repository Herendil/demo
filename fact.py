def fact(n):
    res = 1
    for i in range(n):
        res*=(i+1)
    return res

def coefbin(k,n):
    if(k>=n):
        return(fact(n)/(fact(k)*fact(n-k)))
    else:
        return(0)
