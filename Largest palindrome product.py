
def is_palindrome(n):
    
    s=str(n)
    i=0
    l=len(s)-1
    while i<l:
        if s[i]!=s[l]:
            return False
        else:
            i=i+1
            l=l-1
    return True

m=0
for i in range(999,99,-1):
    for j in range(i,99,-1):
        p=j*i
        if is_palindrome(p)is True:
            print(p,',',i,',',j)
            if p>m:
                m=p

print('THE LARGEST PALINDROME IS,',m)


        

