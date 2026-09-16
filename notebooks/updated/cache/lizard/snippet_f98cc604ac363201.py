def decompress(data):
    d = Decompressor()
    data = d.decompress(data)
    d.finish()
    return data