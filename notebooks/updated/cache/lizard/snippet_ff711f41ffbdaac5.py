def list_to_str(list, separator=','):
    list = [str(x) for x in list]
    return separator.join(list)