#Prime numbers

def is_prime(n):
    for i in range(2,n,1):
        if n%i==0:
            return False

    return True
    
n=int(input("enter a value"))
print(n, " is prime ", is_prime(n))
    

        
