import sys
sys.path.insert(0,'..')

from helper_functions import gen_fibonacci_sequence # very optimized function to produce the sequence

def main():
    
    n = 99999999
    for nth,f_n in enumerate(gen_fibonacci_sequence(n),1):
            if len(str(f_n)) == 1000:
                break

    print(nth) 

if __name__=='__main__':
    main()