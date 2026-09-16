def _encode(cls, value):
    value = json.dumps(value)
    return cls._ENC_RE.sub(lambda x: '%%%2x' % ord(x.group(0)), value)