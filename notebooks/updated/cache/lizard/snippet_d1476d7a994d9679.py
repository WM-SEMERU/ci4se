def limit_unit(timestr, num=2):
    l = len(timestr)
    i = 0
    p = 0
    while i < num and p <= l:
        at = 0
        while p < l:
            c = timestr[p]
            if at == 0:
                if c.isdigit():
                    p += 1
                else:
                    at += 1
            elif at == 1:
                if not c.isdigit():
                    p += 1
                else:
                    at += 1
            else:
                break
        i += 1
    return timestr[:p]