def findunique(lst, key):
    return sorted(set([item[key.lower()] for item in lst]))