i=1

def collatz_sequence(i):
    items=0
    n=[]
    n.append(i)
    while i!=1:
        if i%2==0:
            i=i/2
            n.append(i)
        else:
            i=3*i+1
            n.append(i)
        items=items+1

    print(n)
    return items+1

m=0

for i in range(1,10):
    items=collatz_sequence(i)
    print(i,',',items)
    if items>m:
        m=items
        maxi=i
print(m,',',maxi)

    
    


        
        
    
    
