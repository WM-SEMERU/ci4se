def find_one(cls, pattern, string, flags=0):
    item = re.search(pattern, string, flags=flags)
    return cls(item)