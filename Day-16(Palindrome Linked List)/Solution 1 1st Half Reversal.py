class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rv=None
        fst=slw=head
        while fst and fst.next:
            fst=fst.next.next
            rv,rv.next,slw=slw,rv,slw.next
        if fst:slw=slw.next
        while rv and rv.val==slw.val:
            rv=rv.next
            slw=slw.next
        return not rv
