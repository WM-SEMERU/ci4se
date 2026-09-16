def tagMap(self):
    if self.tagSet:
        return Set.tagMap.fget(self)
    else:
        return self.componentType.tagMapUnique