def fib2(n):
    result=[]
    a, b=0, # -*- coding: latin-1 -*-
    while b < n:
        result.append(b)
        a,b=b, a+b
    return result
f100 = fib2(100)
print f100
    
