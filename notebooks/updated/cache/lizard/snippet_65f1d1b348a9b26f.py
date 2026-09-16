def with_fragment(self, fragment):
    if fragment is None:
        fragment = ''
    elif not isinstance(fragment, str):
        raise TypeError('Invalid fragment type')
    return URL(self._val._replace(fragment=self._FRAGMENT_QUOTER(fragment)),
        encoded=True)