def string(self, *pattern, **kwargs):
    self.pattern(self.build_string(*pattern, **kwargs))
    return self