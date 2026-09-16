def _decode_quadratic_biases(quadratic_string, edgelist):
    quadratic_bytes = base64.b64decode(quadratic_string)
    return {tuple(edge): bias for edge, bias in zip(edgelist, struct.unpack
        ('<' + 'd' * (len(quadratic_bytes) // 8), quadratic_bytes))}