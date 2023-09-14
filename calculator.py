def add(*c):
    return(sum(c))
def sub(a,b):
    return (a-b)
def mul(*b):
    product=1
    for i in b:
        product*=i
    return  product
def div(a,b):
    return a/b
def fac(a):
    fac=1
    i = a
    while i>0:
        fac=fac*i
        i-=1
    return fac
def mod(a,b):
    return a%b
def power(a,c):
    return (a**c)
def per(a,b):
    return (a/b)*100
def fibonacci():
    prv=0
    now=1
    n=int(input("n = "))
    i=0
    print('1')
    while(i<n-1):
    
        tmp = prv + now # summing prv and one next value
        prv = now # assign the previous variable with value of variable one step ahead
        now = tmp #assign the sum of tmp to current variable to be printed
        print(now)
        i+=1
def secret(x):
    y = [(i-4*i)**0.5 for i in x]
    return y
def sum_list(x):
    s=0
    for i in x:
        s+=i
    return s
def nums_in(l,u,s):
    a=[]
    for i in range(l, u, s):
        a.append(i)
    return a
        