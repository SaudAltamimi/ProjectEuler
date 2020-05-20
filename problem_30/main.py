
def is_digits_sum_nth_power(num:int,n:int):
    num_str = str(num)
    return  num == sum(int(d) ** n for d in num_str)

def main():
    
    nums_found = [num 
                  for num in range(2,1_000_000) 
                  if is_digits_sum_nth_power(num,n=5)
                  ]
    
    # the answer 
    print(sum(nums_found))


if __name__ == '__main__':
    main()