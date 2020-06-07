def find_recurring(d):
    l=[]
    R=1
    while R not in l and R!=0:
        l.append(R)
        num=R*10
        R=num%d
    if R==0:
        return 0
    return len(l)

x=0
den=0
for d in range(2,100):
    t=find_recurring(d)
    if t > x:
        den = d
        x=t

print("longest cycle len = ", x, " for denominator = ", den)
    
