def save(self, filething=None):
    fileobj = filething.fileobj
    data = _APEv2Data(fileobj)
    if data.is_at_start:
        delete_bytes(fileobj, data.end - data.start, data.start)
    elif data.start is not None:
        fileobj.seek(data.start)
        fileobj.truncate()
    fileobj.seek(0, 2)
    tags = []
    for key, value in self.items():
        value_data = value._write()
        if not isinstance(key, bytes):
            key = key.encode('utf-8')
        tag_data = bytearray()
        tag_data += struct.pack('<2I', len(value_data), value.kind << 1)
        tag_data += key + b'\x00' + value_data
        tags.append(bytes(tag_data))
    tags.sort(key=lambda tag: (len(tag), tag))
    num_tags = len(tags)
    tags = b''.join(tags)
    header = bytearray(b'APETAGEX')
    header += struct.pack('<4I', 2000, len(tags) + 32, num_tags, HAS_HEADER |
        IS_HEADER)
    header += b'\x00' * 8
    fileobj.write(header)
    fileobj.write(tags)
    footer = bytearray(b'APETAGEX')
    footer += struct.pack('<4I', 2000, len(tags) + 32, num_tags, HAS_HEADER)
    footer += b'\x00' * 8
    fileobj.write(footer)