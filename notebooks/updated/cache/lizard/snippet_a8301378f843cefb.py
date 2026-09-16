def spelling(self):
    if not hasattr(self, '_spelling'):
        self._spelling = conf.lib.clang_getCursorSpelling(self)
    return self._spelling