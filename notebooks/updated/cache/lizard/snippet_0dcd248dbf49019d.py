def decode_call(self, call):
    if call is None:
        return None
    itokens = call.split(self._callables_separator)
    odict = {}
    for key, value in self._clut.items():
        if value in itokens:
            odict[itokens[itokens.index(value)]] = key
    return self._callables_separator.join([odict[itoken] for itoken in itokens]
        )