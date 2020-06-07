fn=1
fn2=2
s=0
while fn<4000000 and fn2<4000000:
    fn3=fn2+fn
    if fn%2==0:
        s=s+fn
        fn=fn2
        fn2=fn3
    else:
        fn=fn2
        fn2=fn3
    

print("THE ANSWER IS",s)
        
        
        
    
    

        
