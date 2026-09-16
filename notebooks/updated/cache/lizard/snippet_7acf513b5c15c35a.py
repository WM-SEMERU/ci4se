def url_decode(s, charset='utf-8', decode_keys=False, include_empty=True,
    errors='replace', separator='&', cls=None):
    if cls is None:
        cls = MultiDict
    return cls(_url_decode_impl(str(s).split(separator), charset,
        decode_keys, include_empty, errors))