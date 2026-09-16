def write_header(self):
    for properties in self.header.values():
        value = properties['value']
        offset_bytes = int(properties['offset'])
        self.file.seek(offset_bytes)
        value.tofile(self.file)