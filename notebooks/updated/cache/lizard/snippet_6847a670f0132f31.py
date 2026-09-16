def assign_indent_numbers(lst, inum, dic=collections.defaultdict(int)):
    for i in lst:
        dic[i] = inum
    return dic