

# print_every_char_nd_ferq_in_sorted_order of a given string



str='geeksforgeeks'

cnt=[0]*26


for i in str:
    cnt[ord(i)-ord('a')]+=1

for i in range(26):
    if(cnt[i]>0):
        print(f"{chr(i+ord('a'))} : {cnt[i]}")

