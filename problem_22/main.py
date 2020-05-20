
def cleanse_string(string:str):
    return string.replace('"','')

def get_ch_score(ch):
    ch = ch.lower() 
    charecters = 'abcdefghijklmnopqrstuvwxyz'
    return charecters.index(ch) + 1

def get_name_score(name:str):
    return sum([get_ch_score(ch) for ch in name])


def main():
    # read the file
    with open('names.txt','r') as f:
        list_names = (cleanse_string(f.read())
                    .split(',')
                    )
    # sort the list into alphabetical order
    list_names = sorted(list_names)
    # calculate based on the question 
    calc_scores = [get_name_score(name) * order 
                   for order,name in enumerate(list_names,start=1)
                   ]

    print(f'The answer --> {sum(calc_scores)}')
    
    

if __name__=='__main__':
    # test get_ch_score 
    # print(get_ch_score('z'))

    main()