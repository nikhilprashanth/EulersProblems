#Non-abundant sums
L=[]
L1=[]
s=0
def abundant_numbers(n):
    s=0
    for i in range(1,int(n/2+1)):
        if n%i==0:
            s=s+i
    if s>n:
        return True
    else:
        return False

def get_all_abundant():
    n=1
    L=[]
    while n<28123:
        qwerty=abundant_numbers(n)
        if qwerty==True:
            #print('abundant number found : ', n)
            L.append(n)
        n=n+1

    print('abundant numbers : ', len(L))
    return L

def get_all_sum_of_abundant(L):
    L1=[]
    for i in range(0,len(L)):
        cur=L[i]
        for j in range(i,len(L)):
            c=cur+L[j]
            if c <= 28123:
                if c not in L1:
                    L1.append(c)

    print('sum of abundant : ', len(L1))
    return L1

def get_sum(L1):
    s=0
    for i in range(1,28123):
        if i not in L1:
            s=s+i
            print(i)
    return s

L=get_all_abundant()
L1=get_all_sum_of_abundant(L)
print("THE ANSWER IS, ", get_sum(L1))


        
    
                  
                  
                  
                   
    


