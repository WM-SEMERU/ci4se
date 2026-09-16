def recursive_map(func, data):

    def recurse(item):
        return recursive_map(func, item)
    items_mapped = map_collection(recurse, data)
    return func(items_mapped)