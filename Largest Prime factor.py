n=int(input('enter a number'))

def is_prime(n):
    for i in range(2,n,1):
        print('is_prime ', i, n)
        if n%i==0:
            print(n," is not prime")
            return False

    print(n, ' is prime')
    return True
    

def find_prime_factors(n):
    prime_factors=[]
    while is_prime(n) is False:
        print('checking ', n)
        for i in range(2,n):
            print("checking divisible ", n, i)
            if n%i==0:
                prime_factors.append(i)
                n=int(n/i)
                break
            
    prime_factors.append(n)
    return prime_factors

p=find_prime_factors(n)
print("prime factors are :", p)n

p.sort(reverse=True)
print('MAXIMUM PRIME FACTOR OF ',n,':',p[0])



