''' 

Checks whether the given number is prime or not. 

'''

def is_prime(x):
    
    # If given number is less than 2 function returns false as 0 & 1 are not primes.
    if x < 2:
        return False
    
    else:
        # Iterate through 2 to number-1.
        for n in range(2, x-1):
            
            # Checks for positive divisor
            if x % n == 0:
                return False
            
        return True
