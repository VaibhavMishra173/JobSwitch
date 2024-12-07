# find best score using bubble sort 66,57,54,53,64,52,and 59

def bubble_sort(score):
    for i in range(len(score)):
        for j in range(len(score)-1):
            if score[j]>score[j+1]:
                # temp=score[j]
                # score[j]=score[j+1]
                # score[j+1]=temp
                score[j],score[j+1]=score[j+1],score[j]


score = [66,57,54,53,64,52,59]

bubble_sort(score)
print(score)