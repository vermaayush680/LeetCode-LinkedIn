def checkInclusion(self, s1: str, s2: str) -> bool:
    l1 = [0]*26
    l2 = [0]*26
    for x in s1:
        l1[ord(x) - ord('a')] += 1

    for i in range(len(s2)):
        print(l1,l2)
        l2[ord(s2[i]) - ord('a')] += 1
        if i >= len(s1):
            l2[ord(s2[i-len(s1)]) - ord('a')] -= 1
        if l1 == l2:
            return True
    return False
