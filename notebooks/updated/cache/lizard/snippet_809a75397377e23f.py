def recarray_view(qimage):
    raw = _qimage_or_filename_view(qimage)
    if raw.itemsize != 4:
        raise ValueError(
            'For rgb_view, the image must have 32 bit pixel size (use RGB32, ARGB32, or ARGB32_Premultiplied)'
            )
    return raw.view(bgra_dtype, _np.recarray)