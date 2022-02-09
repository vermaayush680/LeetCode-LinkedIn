def findPairs(self,nums,k):
    answ=0
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    answ=0
    if k>0:
        for i in d:
            if (i+k) in d:
                answ+=1
    else:
        for i in d:
            answ+=(d[i]>1)       
    return answ
