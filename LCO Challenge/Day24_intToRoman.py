num_map=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]


def n2r(num):
    roman=''
    while num>0:
        for i,r in num_map:
            while num>=i:
                roman+=r
                num-=i
    return roman


julie=int(input("Enter Julie books: "))
nancy=int(input("Enter Nancy books: "))

sum=julie+nancy
rn=n2r(sum)

print(sum,"-->",rn)