def stream_decode_response_unicode(iterator, r):
    encoding = get_encoding_from_headers(r.headers)
    if encoding is None:
        for item in iterator:
            yield item
        return
    decoder = codecs.getincrementaldecoder(encoding)(errors='replace')
    for chunk in iterator:
        rv = decoder.decode(chunk)
        if rv:
            yield rv
    rv = decoder.decode('', final=True)
    if rv:
        yield rv