# https://projecteuler.net/problem=57

from fractions import Fraction
from functools import lru_cache
import tqdm

# we will do it recursivly 
@lru_cache(maxsize = 200) # adding lru cache is really outstanding way to optimize recursion
def expand_fraction(fr:Fraction, n_times : int) -> float:
    '''
    input args:
        number : The base fraction number that we want to expand 
        n_times : how many times we want to expand it

    output args:
        final_decimal : the final floating result
    '''
    assert n_times >= 0, 'Not valid n_times, it should > 0' 

    if n_times == 1 :
        return fr
    
    else:
        numerator = fr.numerator
        denominator = fr.denominator
        n_times -= 1
        new_fr = expand_fraction(fr = fr, n_times= n_times)
        denominator += new_fr
        return numerator/denominator


def n_digits(num:int):
    return len(str(num))


def main():
    f = Fraction('1/2')

    counter = 0
    for i in tqdm.tqdm(range(1,1001)):
        expansion = 1 + expand_fraction(f,n_times=i)
        if n_digits(expansion.numerator) > n_digits(expansion.denominator):
            counter += 1

    print(counter)

if __name__=='__main__':
    main()
