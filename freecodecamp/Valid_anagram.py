# danger
# if each word of one string present in second string return true
# garden 

# a='danger'
# b='garden'

str1="anagram"
str2="nagaram"

di1={}
di2={}

# for i in str1:
#     di1[i]=di1.get(i,0)+1
# print(di1)
# for j in str2:
#     di2[j]=di2.get(j,0)+1
# print(di2)
# if di1.items()==di2.items():
#     print("True")
# else:
#     print("False")

a=sorted(str1)
b=sorted(str2)
print(a)
print(b)
if a==b:
    print("True")
else:
    print("False")
