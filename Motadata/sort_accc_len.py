
input_string = input()
family_list  = input_string.split(" ")
# print("Printing all family member names")

family_list.sort()
family_list.sort(key=len)

# to convert strint list into int list used below line
# family_list=list(map(int, family_list))

family_list=' '.join(map(str, family_list))
print(family_list)


# 1 7 3 4 54 2324 454 322