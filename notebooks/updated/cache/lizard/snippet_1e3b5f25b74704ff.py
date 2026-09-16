def write_var_str(self, value, encoding: str='utf-8'):
    if isinstance(value, str):
        value = value.encode(encoding)
    self.write_var_int(len(value))
    self.write_bytes(value)