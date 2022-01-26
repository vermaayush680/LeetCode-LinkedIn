class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<=1:
            return True
        if ord(word[0]) - ord('a')<0:
            d=1
        else:
            d=0

        if d==0:
            for i in range(1,len(word)):
                if ord(word[i]) - ord('a') <0:
                    return False
        else:
            if ord(word[1]) - ord('a')>=0:
                for i in range(2,len(word)):
                    if ord(word[i]) - ord('a') <0:
                        return False
            else:
                for i in range(2,len(word)):
                    if ord(word[i]) - ord('a')>=0:
                        return False
        return True
