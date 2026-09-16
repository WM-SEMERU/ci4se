def fix_line_breaks(s):
    l = s.splitlines()
    x = [i.strip() for i in l]
    x = [i for i in x if i]
    return '\n'.join(x)