def unit_system_id(self):
    if self._unit_system_id is None:
        hash_data = bytearray()
        for k, v in sorted(self.lut.items()):
            hash_data.extend(k.encode('utf8'))
            hash_data.extend(repr(v).encode('utf8'))
        m = md5()
        m.update(hash_data)
        self._unit_system_id = str(m.hexdigest())
    return self._unit_system_id