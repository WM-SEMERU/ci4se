def split_func(string):
    ind = string.index('(')
    return string[:ind], string[ind + 1:-1].strip('"')