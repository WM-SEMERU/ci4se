def GetHasherClasses(cls, hasher_names=None):
    for hasher_name, hasher_class in iter(cls._hasher_classes.items()):
        if not hasher_names or hasher_name in hasher_names:
            yield hasher_name, hasher_class