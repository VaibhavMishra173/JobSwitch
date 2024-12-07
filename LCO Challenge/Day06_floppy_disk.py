# a floppy disk sows f bites free and u bytes used 
# if you delete a file of size o bytes and create a new file of size n bytes ,how many free bytes will be there in floppy disk ?
# f,u,o and n are user entered value.

def space(f,u,o,n):
    t=f+u
    curr_used=u-o
    curr_used=curr_used+n
    curr_free=t-curr_used
    print(curr_free)


f=int(input("Enter free space in floppy disk: "))
u=int(input("Enter used space in floppy disk: "))
o=int(input("Enter size of file to be deleted in floppy disk: "))
n=int(input("Enter size of new file in floppy disk: "))

space(f,u,o,n)
