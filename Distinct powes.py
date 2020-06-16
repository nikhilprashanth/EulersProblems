#Distinct Powers
l=[]
s=0
c=0
for a in range(2,6,1):
    for b in range(2,6,1):
        s=a**b
        if s not in l:
            l.append(s)
            c=c+1

print(c)
            
            
        
    
