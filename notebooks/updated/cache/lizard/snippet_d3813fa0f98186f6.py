def encode(data, scheme=None, size=None):
    size = size if size else 'ShapeAuto'
    size_name = '{0}{1}'.format(ENCODING_SIZE_PREFIX, size)
    if not hasattr(DmtxSymbolSize, size_name):
        raise PyLibDMTXError('Invalid size [{0}]: should be one of {1}'.
            format(size, ENCODING_SIZE_NAMES))
    size = getattr(DmtxSymbolSize, size_name)
    scheme = scheme if scheme else 'Ascii'
    scheme_name = '{0}{1}'.format(ENCODING_SCHEME_PREFIX, scheme.capitalize())
    if not hasattr(DmtxScheme, scheme_name):
        raise PyLibDMTXError('Invalid scheme [{0}]: should be one of {1}'.
            format(scheme, ENCODING_SCHEME_NAMES))
    scheme = getattr(DmtxScheme, scheme_name)
    with _encoder() as encoder:
        dmtxEncodeSetProp(encoder, DmtxProperty.DmtxPropScheme, scheme)
        dmtxEncodeSetProp(encoder, DmtxProperty.DmtxPropSizeRequest, size)
        if dmtxEncodeDataMatrix(encoder, len(data), cast(data, c_ubyte_p)
            ) == 0:
            raise PyLibDMTXError(
                'Could not encode data, possibly because the image is not large enough to contain the data'
                )
        w, h, bpp = map(partial(dmtxImageGetProp, encoder[0].image), (
            DmtxProperty.DmtxPropWidth, DmtxProperty.DmtxPropHeight,
            DmtxProperty.DmtxPropBitsPerPixel))
        size = w * h * bpp // 8
        pixels = cast(encoder[0].image[0].pxl, ctypes.POINTER(ctypes.
            c_ubyte * size))
        return Encoded(width=w, height=h, bpp=bpp, pixels=ctypes.string_at(
            pixels, size))