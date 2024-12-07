def printAllCombination(sarray):
    if len(sarray)==0:
        return[]
    if len(sarray)==1:
        return[sarray]
    l=[]
    for i in range(len(sarray)):
        m=sarray[i]
        remLst=sarray[:i]+sarray[i+1:]
        for p in printAllCombination(remLst):
            l.append([m]+p)
    
    return l   


a=["ram","anuj","deepak","ravi"]

for combination in printAllCombination(a):
    print(combination)