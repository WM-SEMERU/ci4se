def _convert_default_value(self, default):
    if default is None:
        return None
    if isinstance(default, str):
        if self.special_type == 'string':
            return default.encode('utf-8') + b'\x00'
        raise DataError(
            'You can only pass a unicode string if you are declaring a string type config variable'
            , default=default)
    if isinstance(default, (bytes, bytearray)):
        if self.special_type == 'string' and isinstance(default, bytes):
            default += b'\x00'
        return default
    if isinstance(default, int):
        default = [default]
    format_string = '<' + self.base_type * len(default)
    return struct.pack(format_string, *default)