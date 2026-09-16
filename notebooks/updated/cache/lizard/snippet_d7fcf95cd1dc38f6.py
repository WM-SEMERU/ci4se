def _calculateEncodingKey(comparator):
    encodingName = None
    for k, v in list(_encodings.items()):
        if v == comparator:
            encodingName = k
            break
    return encodingName