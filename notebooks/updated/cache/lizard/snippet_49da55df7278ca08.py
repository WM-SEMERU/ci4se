def incr(l, cap):
    l[0] = l[0] + 1
    for i in range(len(l)):
        if l[i] > cap[i] and i < len(l) - 1:
            l[i] = 0
            l[i + 1] = l[i + 1] + 1
        elif l[i] > cap[i] and i == len(l) - 1:
            l = -1
    return l