print("Type 1\n")
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
for i in range(5):
    for j in range(i):
        print(i,end=" ")
    print('\r')

print("\nType 2\n")
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
num=1
for i in range(5):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print('\r')
    
print("\ntype 3\n")
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
for i in range(5):
    for j in range(i+1):
        print('*',end=" ")
    print()

print("\ntype 4\n")
# *
# **
# ***
# ****
# *****
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()

