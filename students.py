
import random as ran
def add_std(n,names,rolls):  
    n=n.lower()
    names.append(n)
    rolls.append(ran.randint(100,999))
    return names,rolls
def get_std(r,names,rolls):
    
    a=False
    b=False
    for i in range(0,len(rolls)):
        if rolls[i] == r:
            a=rolls[i]
            b=names[i]
    
    return b,a
            
    
def search_std(r,names,rolls):
    yes=0
    for j in range(0,len(rolls)):
            if rolls[j] == r:
                yes+=1     
        
    return yes==1
        
def remove_std(r,names,rolls):
    r = int(r)
    yes=0
    a=0
    b=0
    for i in range(len(rolls)):
        if rolls[i] == r:
            a = rolls[i]
            b = names[i]
            yes+=1
        
            
    if(yes!=1):
        return "Not Found"
    rolls.remove(a)
    names.remove(b)
    return names,rolls
        
    
def display_rec(names,rolls):
    print(names)
    print(rolls)

def change(n):
    n.append(100)
    del n[0]

