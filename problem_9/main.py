
def is_specific_condition(a,b,c):
    '''this function can be used to implment any chosen condition'''
    return a + b + c == 1000

def gen_pythagorean_triplet_numbers():
    '''
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2
    '''
    for a in range(1,999):
        for b in range(a,999):
            c = float((a**2 + b**2)**0.5)
            if c.is_integer(): # c has to be natural number
                yield a,b,int(c)
            

def main():

    # generate pythagorean triplet numbers and filter by condition 
    # --> multibly abc once you find 
    # --> sum
    print(sum(a*b*c 
              for a,b,c in gen_pythagorean_triplet_numbers() 
              if is_specific_condition(a,b,c)
              )
         )


if __name__ == '__main__':
    main()