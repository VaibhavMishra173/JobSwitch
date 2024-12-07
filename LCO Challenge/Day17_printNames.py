# there are 10 students in class osme students are same ,print the name that occur more than one time. all name should be in single string.


def find_dup(a):
    x=a.split()
    size=len(x)
    repeated=[]
    for i in range(size):
        k=i+1
        for j in range(k,size):
            if x[i]==x[j] and x[i] not in repeated:
                repeated.append(x[i])
                print(x[i])

str="Aman Ankit Deepak Aman Arjun Nakul Amit Priyanshu Vansh Rajat Sagar"

find_dup(str)


