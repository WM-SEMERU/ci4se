def tobinarray(self, start=None, end=None, pad=_DEPRECATED, size=None):
    if not isinstance(pad, _DeprecatedParam):
        print("IntelHex.tobinarray: 'pad' parameter is deprecated.")
        if pad is not None:
            print('Please, use IntelHex.padding attribute instead.')
        else:
            print("Please, don't pass it explicitly.")
            print(
                'Use syntax like this: ih.tobinarray(start=xxx, end=yyy, size=zzz)'
                )
    else:
        pad = None
    return self._tobinarray_really(start, end, pad, size)