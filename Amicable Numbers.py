#Amicable Numbers
s=0
L=[]
def sum_of_divisors(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s

for n in range(1,10001):
    w=sum_of_divisors(n)
    w1=sum_of_divisors(w)
    if w1==n:
        if n not in L and w not in L:
            print(n,',',w)
        if n not in L:
            s=s+n
            L.append(n)
        if w not in L:
            s=s+w
            L.append(w)        
        

print(s)
