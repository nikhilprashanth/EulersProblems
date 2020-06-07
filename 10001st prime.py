#10001st prime
c=0
n=2
def is_prime(n):
    for i in range(2,n,1):  
        if n%i==0:
            return False

    return True

while c<=10000:
    if is_prime(n) is True:
        c=c+1
        n=n+1
    else:
        n=n+1

print('THE 10001st PRIME IS: ',n-1)
    
    
    
