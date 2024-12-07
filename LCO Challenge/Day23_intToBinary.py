
def binary(a):
    l=""
    l+=(str(a%2))
    if a==0:
        return
    if a>0:
        binary(int(a/2))
    print(l)


binary(12)

