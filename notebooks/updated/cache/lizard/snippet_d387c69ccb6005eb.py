def deserialize(self, value, flags):
    FLAGS = self.FLAGS
    if flags & FLAGS['compressed']:
        value = self.compression.decompress(value)
    if flags & FLAGS['binary']:
        return value
    if flags & FLAGS['integer']:
        return int(value)
    elif flags & FLAGS['long']:
        return long(value)
    elif flags & FLAGS['object']:
        buf = BytesIO(value)
        unpickler = self.unpickler(buf)
        return unpickler.load()
    if six.PY3:
        return value.decode('utf8')
    try:
        value.decode('ascii')
    except UnicodeDecodeError:
        try:
            return value.decode('utf8')
        except UnicodeDecodeError:
            return value
    else:
        return value