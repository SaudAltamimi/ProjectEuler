# a general common functions that are used in many projectauler problems

def is_prime(num:int):
    # a prime number is a number that is divisible by only itself and 1
    # if all the numbers between 2 and num/2 are not divisons of num then num is a prime number 
    return not any(num%i==0 for i in range(2,int(num/2)+1))