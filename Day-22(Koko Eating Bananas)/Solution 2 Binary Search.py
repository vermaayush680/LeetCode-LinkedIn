l,r=1,10**9
while(l<r):
    m=l+(r-l)//2
    a=0
    for p in piles:
        a+=(p+m-1)//m
    if a>h:
        l=m+1
    else:
        r=m
return l
