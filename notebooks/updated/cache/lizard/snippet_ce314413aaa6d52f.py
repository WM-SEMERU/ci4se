def toStringArray(name, a, width=0):
    string = name + ': '
    cnt = 0
    for i in a:
        string += '%4.2f  ' % i
        if width > 0 and (cnt + 1) % width == 0:
            string += '\n'
        cnt += 1
    return string