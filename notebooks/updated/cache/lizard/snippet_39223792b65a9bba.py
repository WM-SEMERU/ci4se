def __EncodedAttribute_decode_gray16(self, da, extract_as=ExtractAs.Numpy):
    if hasattr(da, 'value'):
        raise TypeError(
            "DeviceAttribute argument must have been obtained from a call which doesn't extract the contents"
            )
    if extract_as not in _allowed_extract:
        raise TypeError('extract_as must be one of Numpy, String, Tuple, List')
    return self._decode_gray16(da, extract_as)