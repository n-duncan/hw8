#
# Did you receive any help whatsoever from anyone in solving this assignment?
# [No]
#
# Did you give any help whatsoever to anyone in solving this assignment?
# [No]
#
def explicit_exponentiation(a, b):
    # TODO: Find a to the power of b, using an explicit algorithm
    product = 1.0
    if(b == 0):
        return 1
    else:
        for x in range(abs(b)):
            product *= a
    if(b > 0):
        return product
    else:
        return (1.0 / product)

def recursive_exponentiation(a, b):
    # TODO: Find a to the power of b using a recursive algorithm
    if(b == 0): 
        return 1.0 # for exponents of 0
    elif(b > 0):
        return float(a * recursive_exponentiation(a, b-1)) # for exponents greater than 0
    else:
        return float(recursive_exponentiation(a, b+1)) / a # for exponenets less than 0

    
def gcd(a, b):
    # TODO: Find gcd of a and b
    # Using the Euclidean algorithm for finding gcd
    if(abs(a) % abs(b) == 0): # if a divis by b then return
        return b
    else: # else try again with the divisor and the remainder of divison
        return gcd(b, a % b) 

def find_primes(n):
    # TODO: Find all primes up to n
    primes = []
    for x in range(2,n+1):
        primes.append(x)
    index = 0
    if(len(primes) <= 1):
        return primes
    else:
        x = primes[index]
    while(x < (n ** (1.0/2))):
        for y in primes:
            if(y % x == 0 and y != x):
                primes.remove(y)
        x+=1
    return primes
    
def greatest_prime_factor(n):
    # TODO: Find the greatest prime factor for n
    #find primes less than square root
    primes = find_primes(int(n ** (1.0 / 2)))
    prime = 1
    while(len(primes) > 0):
        prime = primes[0]
        if(n % prime == 0):
            n = n / prime
        elif(n == 1):
            return prime
        else:
            primes.remove(prime)
    #if greatest prime not < sqrt(n)
    return int(n)


#TESTING AREA --------
"""
print("Testing GCD")

for x in range(2053,2567):
    for y in range(1520,1789):
        print(str(x) + " " + str(y))
        print(gcd(x,y))
        print("\n")

print(find_primes(100))
"""

#print(greatest_prime_factor(100))
