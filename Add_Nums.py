def addNums(l1,l2):
    l1 = l1[::-1]
    l1 = [str(i) for i in l1]
    l2 = l2[::-1]
    l2 = [str(i) for i in l2]

    l3 = str(int("".join(l1)) + int("".join(l2)))
    l3 = [int(i) for i in l3]
    return l3[::-1]


res = addNums([2,4,3],[5,6,4])
print(res)