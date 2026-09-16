def description(self):
    for e in self:
        if isinstance(e, Description):
            return e.value
    raise NoSuchAnnotation