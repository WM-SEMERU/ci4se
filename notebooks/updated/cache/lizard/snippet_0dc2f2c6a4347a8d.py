def to_list(item_or_list):
    if isinstance(item_or_list, list):
        return item_or_list
    elif isinstance(item_or_list, (str, bytes)):
        return [item_or_list]
    elif isinstance(item_or_list, Iterable):
        return list(item_or_list)
    else:
        return [item_or_list]