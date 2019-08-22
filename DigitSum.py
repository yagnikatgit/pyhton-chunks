''' 

Results into sum of all digits. 

'''

def digit_sum(x):
    total = 0
    
    # While there is atleast 1 digit loop will continue.
    while x > 0:
        
        # Mudulo by 10 gives last digit of the given number.
        total += x % 10
        
        # Use of classic division (e.g. 5//2 = 2)
        # Gives all digits except last one.
        x = x // 10
    
    return total

print(digit_sum(1439))
print(x//10)
