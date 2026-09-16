def __EncodedAttribute_generic_encode_rgb24(self, rgb24, width=0, height=0,
    quality=0, format=_ImageFormat.RawImage):
    if not is_seq(rgb24):
        raise TypeError(
            'Expected sequence (str, numpy.ndarray, list, tuple or bytearray) as first argument'
            )
    is_str = is_pure_str(rgb24)
    if is_str:
        if not width or not height:
            raise ValueError(
                'When giving a string as data, you must also supply width and height'
                )
    if np and isinstance(rgb24, np.ndarray):
        if rgb24.ndim != 3:
            if not width or not height:
                raise ValueError(
                    'When giving a non 2D numpy array, width and height must be supplied'
                    )
            if rgb24.nbytes / 3 != width * height:
                raise ValueError('numpy array size mismatch')
        elif rgb24.itemsize != 1:
            raise TypeError('Expected numpy array with itemsize == 1')
        if not rgb24.flags.c_contiguous:
            raise TypeError(
                'Currently, only contiguous, aligned numpy arrays are supported'
                )
        if not rgb24.flags.aligned:
            raise TypeError(
                'Currently, only contiguous, aligned numpy arrays are supported'
                )
    if not is_str and (not width or not height):
        height = len(rgb24)
        if height < 1:
            raise IndexError('Expected sequence with at least one row')
        row0 = rgb24[0]
        if not is_seq(row0):
            raise IndexError(
                'Expected sequence (str, numpy.ndarray, list, tuple or bytearray) inside a sequence'
                )
        width = len(row0)
        if is_pure_str(row0) or type(row0) == bytearray:
            width /= 3
    if format == _ImageFormat.RawImage:
        self._encode_rgb24(rgb24, width, height)
    elif format == _ImageFormat.JpegImage:
        self._encode_jpeg_rgb24(rgb24, width, height, quality)