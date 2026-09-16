def tobinfile(self, fobj, start=None, end=None, pad=_DEPRECATED, size=None):
    if not isinstance(pad, _DeprecatedParam):
        print("IntelHex.tobinfile: 'pad' parameter is deprecated.")
        if pad is not None:
            print('Please, use IntelHex.padding attribute instead.')
        else:
            print("Please, don't pass it explicitly.")
            print(
                'Use syntax like this: ih.tobinfile(start=xxx, end=yyy, size=zzz)'
                )
    else:
        pad = None
    if getattr(fobj, 'write', None) is None:
        fobj = open(fobj, 'wb')
        close_fd = True
    else:
        close_fd = False
    fobj.write(self._tobinstr_really(start, end, pad, size))
    if close_fd:
        fobj.close()