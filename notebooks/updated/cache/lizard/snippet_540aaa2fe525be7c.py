def read_table(self):
    self.bitcount = self.bits = 0
    tlen = unpack('>I', self.input.read(4))[0]
    table_data = AMQPReader(self.input.read(tlen))
    result = {}
    while table_data.input.tell() < tlen:
        name = table_data.read_shortstr()
        ftype = ord(table_data.input.read(1))
        if ftype == 83:
            val = table_data.read_longstr()
        elif ftype == 73:
            val = unpack('>i', table_data.input.read(4))[0]
        elif ftype == 68:
            d = table_data.read_octet()
            n = unpack('>i', table_data.input.read(4))[0]
            val = Decimal(n) / Decimal(10 ** d)
        elif ftype == 84:
            val = table_data.read_timestamp()
        elif ftype == 70:
            val = table_data.read_table()
        else:
            raise ValueError('Unknown table item type: %s' % repr(ftype))
        result[name] = val
    return result