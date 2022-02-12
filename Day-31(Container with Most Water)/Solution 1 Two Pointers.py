def maxArea(self, height: List[int]) -> int:
    l,r=0,len(height)-1
    c=0
    while(l<r):
        h=min(height[l],height[r])
        c=max(c,h*(r-l))
        l+=(height[l]==h)
        r-=(height[r]==h)
    return c
