def IndexOfNth(s, value, n):
    remaining = n
    for i in xrange(0, len(s)):
        if s[i] == value:
            remaining -= 1
            if remaining == 0:
                return i
    return -1