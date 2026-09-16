def read_gzipped_text_url(url):
    import urllib2
    import zlib
    from StringIO import StringIO
    opener = urllib2.build_opener()
    request = urllib2.Request(url)
    request.add_header('Accept-encoding', 'gzip')
    respond = opener.open(request)
    compressedData = respond.read()
    respond.close()
    opener.close()
    compressedDataBuf = StringIO(compressedData)
    d = zlib.decompressobj(16 + zlib.MAX_WBITS)
    buffer = compressedDataBuf.read(1024)
    s = []
    while buffer:
        s.append(d.decompress(buffer))
        buffer = compressedDataBuf.read(1024)
    s = ''.join(s)
    return s