class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        d="A"<=word[0]<="Z"
        c=0
        for i in word:
            c+=("A"<=i<="Z")
        if c==len(word) or c==0 or (c==1 and d==1):
            return True
        else:
            return False
