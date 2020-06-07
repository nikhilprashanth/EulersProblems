
def length_1to99(n):
    d={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}
    if n in d:
        return d[n]
    else:
        w=int(n/10)
        w2=int(n%10)
        w3=int(d[w2]+d[w*10])
        return w3

def length_100to999(n):
    d={100:10,200:10,300:12,400:11,500:11,600:10,700:12,800:12,900:11,1000:11}
    if n in d:
        return d[n]
    else:
        q=int(n/100)
        q2=int(n%100)
        l=length_1to99(q2)
        q3=int(d[q*100]+l+3)
        return q3
    
s=0
for n in range(1,1001):
    if n<=99:
        r=length_1to99(n)
    else:
        r=length_100to999(n)
    s=r+s

print("THE ANSWER IS",',',s)
