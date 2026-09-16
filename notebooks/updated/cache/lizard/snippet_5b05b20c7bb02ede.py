def cast_out(self, klass):
    if _debug:
        SequenceOfAny._debug('cast_out %r', klass)
    if not issubclass(klass, List):
        raise DecodingError('%r is not a list' % (klass,))
    helper = klass()
    t = TagList(self.tagList[:])
    helper.decode(t)
    if len(t) != 0:
        raise DecodingError('incomplete cast')
    return helper.value