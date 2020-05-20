# refer to the link to read the question: https://projecteuler.net/problem=41
import sys
sys.path.insert(0,'..')

from helper_functions import is_prime

# Python function to print permutations of a given list 
def permutation(lst:list): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  rem_lst is 
       # remaining list 
       rem_lst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(rem_lst): 
           l.append([m] + p)

    return l

def gen_pandigital(digits_len:int):
    if digits_len == 0:
        raise ValueError('Digits_len must be greater then 0')

    base_digits = [str(i) for i in range(1,digits_len+1)]

    all_possible_pandigital_lists = permutation(base_digits)

    all_possible_pandigital = [''.join(l) for l in all_possible_pandigital_lists]   
        
    return [int(num) for num in all_possible_pandigital]



def main():
    max_found = 1
    for digits_len in range(1,9):
        for pand in gen_pandigital(digits_len):
            if is_prime(pand) and pand > max_found:
                max_found = pand

    
    print(f'Gotcha !!! --> {max_found}')

if __name__=='__main__':
    main()