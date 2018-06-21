''' 

Generates (using generator) n fibonacci numbers. 

'''

def fibo(n):
    a = 0
    b = 1
    
    # Using generator; yield keyword yields or froze the state of generator. 
    for i in range(n):
        yield a
        
        # Swapping take place
        a,b = b, a+b


# Print all values in once.
for num in fibo(5):
    print(num)
    
# OR
# Use next() for generator as you go.
fibonacci = fibo(5)
next(fibonacci)
