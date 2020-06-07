#Special pythagorean triplet
n=1000
for c in range(1,n+1):
    for b in range(1,c):
        for a in range(1,b):
            s=a+b+c
            a2=a**2
            b2=b**2
            c2=c**2
            if s==n and a2+b2==c2:
                p=a*b*c
                print(a,',',b,',',c)
                print('THE PRODUCT IS',',',p)
            
            
        
    

    
        
            
        
    
    
    
    


    
