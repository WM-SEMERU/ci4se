def _serialize_normalized_array(array, fmt='png', quality=70):
    dtype = array.dtype
    assert np.issubdtype(dtype, np.unsignedinteger)
    assert np.max(array) <= np.iinfo(dtype).max
    assert array.shape[-1] > 1
    image = PIL.Image.fromarray(array)
    image_bytes = BytesIO()
    image.save(image_bytes, fmt, quality=quality)
    image_data = image_bytes.getvalue()
    return image_data