def compressBuffer(buffer):
    zbuf = cStringIO.StringIO()
    zfile = gzip.GzipFile(mode='wb', fileobj=zbuf, compresslevel=9)
    zfile.write(buffer)
    zfile.close()
    return zbuf.getvalue()