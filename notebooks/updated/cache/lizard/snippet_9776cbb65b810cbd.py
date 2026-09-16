def _get_struct_string(self):
    data = []
    while True:
        t = self._src.read(1)
        if t == b'\x00':
            break
        data.append(t)
    val = b''.join(data)
    return val.decode('utf8')