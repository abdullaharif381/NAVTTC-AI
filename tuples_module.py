def to_list(*t):
    lis=[]
    for i in t:
        lis.append(i)
    return lis
def count_even(*t):
    count=0
    for i in t:
        if i%2==0:
            count+=1
            
    return count
def above_20(*t):
    count=0
    a=[]
    for i in t:
        if i>20:
            a.append(i)       
            
    return a