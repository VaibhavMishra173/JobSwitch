
def check(str):
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    len_of_string=len(str)
    res=[1]*len_of_string
    for i in range(len_of_string):
        for char in alpha:
            if char not in str[i].lower():
                res[i]=0
                
    print(res)

str=["The quick brown fox jumps over the little lazy","The quick brown fox jumps over the little lazy dog","The quick brown fox jumps over the little lazy do"]
check(str)
