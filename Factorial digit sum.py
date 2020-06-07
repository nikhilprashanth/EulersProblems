s=1
s2=0
for i in range(1,101):
    s=s*i

q=str(s)
w=len(q)
for n in range(0,w):
    s2=int(q[n])+s2

print("THE ANSWER IS, ",s2)
print(s)
