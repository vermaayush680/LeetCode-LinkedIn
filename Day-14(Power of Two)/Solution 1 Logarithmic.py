def isPowerOfTwo(self, n: int) -> bool:
    if n<=0:
        return False
    a=int(m.log2(n))
    return 2**a == n
