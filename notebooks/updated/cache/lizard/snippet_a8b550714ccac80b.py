def compile(self, s):
    f = io.BytesIO()
    for t in s.split():
        t_up = t.upper()
        if t_up in self.opcode_to_int:
            f.write(int2byte(self.opcode_to_int[t]))
        elif 'OP_%s' % t_up in self.opcode_to_int:
            f.write(int2byte(self.opcode_to_int['OP_%s' % t]))
        elif t_up.startswith('0X'):
            d = binascii.unhexlify(t[2:])
            f.write(d)
        else:
            v = self.compile_expression(t)
            self.write_push_data([v], f)
    return f.getvalue()