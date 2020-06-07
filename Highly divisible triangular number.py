#Highly divisible triangular number

def find_factors(n):
    factors=[]
    for i in range(1,n):
        if n%i==0:
            factors.append(i)
    return factors

n=1
s=0
i=1

while 1:
    n=s+i
    s=n
    i=i+1
    f=find_factors(n)
    print(n, len(f))
    if len(f)>=500:
        print(n,',',f)
        break
        




     
    
    
