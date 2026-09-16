def extract(code, tree, prefix=[]):
    if isinstance(tree, list):
        l, r = tree
        prefix.append('0')
        extract(code, l, prefix)
        prefix.pop()
        prefix.append('1')
        extract(code, r, prefix)
        prefix.pop()
    else:
        code[tree] = ''.join(prefix)