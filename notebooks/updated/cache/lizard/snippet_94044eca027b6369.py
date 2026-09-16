def RegisterDecompressor(cls, decompressor):
    compression_method = decompressor.COMPRESSION_METHOD.lower()
    if compression_method in cls._decompressors:
        raise KeyError(
            'Decompressor for compression method: {0:s} already set.'.
            format(decompressor.COMPRESSION_METHOD))
    cls._decompressors[compression_method] = decompressor