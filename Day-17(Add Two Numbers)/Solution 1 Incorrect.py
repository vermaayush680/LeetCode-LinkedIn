class Solution:
def addTwoNumbers(self,l1,l2):
    l3=l1
    temp=l3
    carry=0
    while l1 and l2:
        l3.val=l1.val+l2.val+carry
        carry=l3.val//10
        l3.val=l3.val%10
        l1=l1.next
        l2=l2.next
        l3=l3.next
    return temp
