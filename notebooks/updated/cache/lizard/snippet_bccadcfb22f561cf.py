def hasannotation(self, Class, set=None):
    return sum(1 for _ in self.select(Class, set, True,
        default_ignore_annotations))