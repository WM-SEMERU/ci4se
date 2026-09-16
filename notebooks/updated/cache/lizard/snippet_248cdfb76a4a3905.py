def tags(self, *names):
    if len(names) == 1 and isinstance(names[0], list):
        names = names[0]
    return TaggedCache(self, TagSet(self, names))