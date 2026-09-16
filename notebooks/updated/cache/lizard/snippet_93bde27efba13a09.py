def read_items(group, version='1.1', check=False):
    if version == '0.1':
        return ''.join([unichr(int(c)) for c in group['files'][...]]).replace(
            '/-', '/').split('/\\')
    elif version == '1.0':
        return Items(list(group['files'][...]), check)
    else:
        return Items(list(group['items'][...]), check)