import random, math, time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        return result, f'{elapsed:.6f}'
    return wrapper

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True  

def prev_prime(num):
    candidate = num - 1
    while candidate >= 2:
        if is_prime(candidate):
            return candidate
        candidate -= 1
    return 2

@timer
def prime_arr(array):
    for i in range(len(array)):
        array[i] = prev_prime(array[i])
        
def main(*args):
    result = []
    
    for arg in args:
        array = [random.randint(1000,5000) for i in range(arg)]
        result.append(prime_arr(array)[1])
    
    print(result)
    return result