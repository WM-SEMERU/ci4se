def find(pattern, root=os.curdir):
    hits = ''
    for F in locate(pattern, root):
        hits = hits + F + '\n'
    l = hits.split('\n')
    if not len(l[-1]):
        l.pop()
    if len(l) == 1 and not len(l[0]):
        return None
    else:
        return l