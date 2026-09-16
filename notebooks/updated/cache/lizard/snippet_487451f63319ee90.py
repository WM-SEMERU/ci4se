def include(self, filename, *args, **kwargs):
    p = self.__class__(filename, skip_defaults=True, skip_fallbacks=True)
    self.update(p._sections, *args, **kwargs)