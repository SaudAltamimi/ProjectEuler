
def gen_fibonacci_sequence(n:int):
    '''
    A fibonacci sequence generator
    INPUTS:
        n: the number of terms to generate 
    OUTPUTS:
        fibonacci_sequence: the fibonacci sequence generator
    '''
    f_n_minus_one = 1
    f_n = 1
    if n == 1:
        yield f_n_minus_one
    elif n == 2:
        yield f_n_minus_one
        yield f_n
    else:
        yield f_n_minus_one
        yield f_n
        
        for i in range(3,n+1):
            f_n,f_n_minus_one= (f_n + f_n_minus_one,f_n)
            yield f_n
            


