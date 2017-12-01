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
        return 1
    elif(b > 0):
        return a * recursive_exponentiation(a, b-1)
    else:
        return (1.0 / a) * recursive_exponentiation(a, b+1)

    
def gcd(a, b):
    # TODO: Find gcd of a and b
    x = 1
    gcd = 1
    while(True):
        if(x > a or x > b):
            return gcd
        else:
            if(a % x == 0 and b % x == 0):
                gcd = x
            x += 1
    
"""
def find_primes(n):
    # TODO: Find all primes up to n


def greatest_prime_factor(n):
    # TODO: Find the greatest prime factor for n
"""

#TESTING AREA --------

print("Testing Exponentiation")

print(explicit_exponentiation(1,3))
print(explicit_exponentiation(5,6))
print(explicit_exponentiation(5,-1))
print(explicit_exponentiation(3,0))

print("Testing Recursive Exponentiation")

print(recursive_exponentiation(1,3))
print(recursive_exponentiation(5,6))
print(recursive_exponentiation(5,-1))
print(recursive_exponentiation(3,0))

print("Testing GCD")

print(gcd(1,3))
print(gcd(5,125))
print(gcd(30,60))
print(gcd(47,156))
