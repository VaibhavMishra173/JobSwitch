


distance=float(input('Enter distance'))
# time=input('Enter time in HH MM SS: ')
# time=time.split(" ")
# time=list(map(int,time))
# print(time)
hh=float(input('enter hour'))
mm=float(input('enter minutes'))
ss=float(input('enter seconds'))

time_Seconds=(hh*3600)+(mm*60)+ss
kph=(distance/1000.0)/(time_Seconds/3600.0)
mph=kph/1.609

print(f"Your speed in miles/hour is {mph}")
