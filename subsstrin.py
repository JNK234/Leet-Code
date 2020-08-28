# def lengthSub(s):
#     lst = list(s)
#     subs = []
#     for i in range(len(lst)):
#         strr = lst[i] 
#         for j in range(i+1,len(lst)-1):
#             if lst[j] in strr:
#                 continue
#             else:
#                 strr = strr + lst[j]
#         print(strr)

def lengthSub(s):
    lst = list(s)
    subs = []
    if lst:
        for i in range(len(lst)):
            strr = lst[i] 
            for j in range(i+1,len(lst)):
                if lst[j] in strr:
                    break
                else:
                    strr = strr + lst[j]
            subs.append(strr)
        subs = [len(i) for i in subs]
        return max(subs)
    else:
        return 0
   



# s = "pwwkew"
s = 'au'
# s = "abcabcbb"
print(lengthSub(s))
