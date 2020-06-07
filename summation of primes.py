#Summation of primes
n=2
l=2000000
s=0
def is_prime(n):
    for i in range(2,n,1):  
        if n%i==0:
            return False

    return True

while n<l:
    if is_prime(n) is True:
        s=s+n
        print(n)
    n=n+1

print('THE SUM IS',',',s)
    
        

