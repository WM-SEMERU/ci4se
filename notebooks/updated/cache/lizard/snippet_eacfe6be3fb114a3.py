def _write_bin(self, stream, byte_order):
    for rec in self.data:
        for prop in self.properties:
            prop._write_bin(rec[prop.name], stream, byte_order)