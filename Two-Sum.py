      
def addNums(nums,target):
    tups = list(enumerate(nums))
    for i in range(len(tups)-1):
        for j in range(i+1,len(tups)):
            if tups[i][1] + tups[j][1] == target:
                return [tups[i][0],tups[j][0]]



nums = [2,7,11,15]
target = 9
res = addNums(nums,target)
print(res)