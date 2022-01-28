class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        while head:
            l+=[str(head.val)]
            head = head.next
        return l==l[::-1]
