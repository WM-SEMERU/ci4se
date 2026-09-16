def add_header_name(self, header_name, is_indexed=False):
    header = ConfigHeader()
    header.is_indexed = is_indexed
    self.headers[header_name] = header
    return header