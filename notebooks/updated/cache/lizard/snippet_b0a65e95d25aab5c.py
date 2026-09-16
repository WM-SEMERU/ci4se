def list_pp(ll, separator='|', header_line=True, autonumber=True):
    if autonumber:
        for cnt, i in enumerate(ll):
            i.insert(0, cnt if cnt > 0 or not header_line else '#')

    def lenlst(l):
        return [len(str(i)) for i in l]
    lst_len = [lenlst(i) for i in ll]
    lst_rot = zip(*lst_len[::-1])
    lst_len = [max(i) for i in lst_rot]
    frmt = separator + separator.join([('{!s:' + str(i) + '}') for i in
        lst_len]) + separator
    if header_line:
        header_line = '-' * len(frmt.format(*ll[0]))
    for cnt, l in enumerate(ll):
        if cnt < 2 and header_line:
            print(header_line)
        print(frmt.format(*l))
    if header_line:
        print(header_line)
    return lst_len