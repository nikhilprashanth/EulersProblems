#Digit fifth powers
n=int(input("number  "))

def function4(i,s):
    if s==i:
        return True
    else:
        return False

def function3(Nikhil):
    sabasito=len(Nikhil)
    s=0
    for v in range(0,sabasito-1):
        s=Nikhil[v]+s
    qwerty=function4(i,s)
    return qwerty

       
def function2(n,l):
    Nikhil=[]
    o=len(l)
    for x in range(0,o-1):
        y=l[x]**n
        Nikhil.append(y)
        x=x+1
    good=function3(Nikhil)
    return good
     

def function(i):
    l=[]
    while len(str(i))!=1:
        e=len(str(i))
        e2=10**(e-1)
        e3=int(i/e2)
        l.append(e3)
        i=i-e2
    if len(str(i))==1:
        l.append(i)
    
    legokid=function2(n,l)
    return legokid
    
    
    
s=1
for i in range(1,1635):
    hi=function(i)
    if hi=="True":
        s=i+s

print("THE SUM IS ",s-1)
