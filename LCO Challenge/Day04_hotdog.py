
# find total number of pack in 400 hotdog without using 5 and / 



total=400
onepack=8
count=0

while(total>=onepack):
    total=total-onepack
    count+=1
print(count)