def pretty(self):
    retval = (
        'Key(name={}, type={}, listable={}, compare={}, priority={}, kind_preference={}, replace_better={})'
        .format(self.name, self.type, self.listable, self.compare, self.
        priority, self.kind_preference, self.replace_better))
    return retval