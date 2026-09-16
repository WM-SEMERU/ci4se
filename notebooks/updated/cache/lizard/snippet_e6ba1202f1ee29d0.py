def ldContains(self, what, key):
    if isListKey(key):
        i = listKeyIndex(key)
        return i < len(what) and what[i] != missing_value
    else:
        return key in what and what[key] != missing_value