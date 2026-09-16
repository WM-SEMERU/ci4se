def write_struct_field(self, struct_name, field_name, values, x, y, p=0):
    field, address, pack_chars = self._get_struct_field_and_address(struct_name
        , field_name)
    if field.length != 1:
        assert len(values) == field.length
        data = struct.pack(pack_chars, *values)
    else:
        data = struct.pack(pack_chars, values)
    self.write(address, data, x, y, p)