#Number Spiral Diagonals
n=int(input("Enter grid size "))
e=8
i=1
s=1

while i!=int(n*n):
    d1=i+e/4
    d2=i+2*e/4
    d3=i+3*e/4
    d4=i+4*e/4
    s=d1+d2+d3+d4+s
    e=e+8
    i=d4

print('The sum of the diagonals = ',s)
    
