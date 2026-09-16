def get_msgbuf(self):
    values = []
    for i in range(len(self.fmt.columns)):
        if i >= len(self.fmt.msg_mults):
            continue
        mul = self.fmt.msg_mults[i]
        name = self.fmt.columns[i]
        if name == 'Mode' and 'ModeNum' in self.fmt.columns:
            name = 'ModeNum'
        v = self.__getattr__(name)
        if mul is not None:
            v /= mul
        values.append(v)
    return struct.pack('BBB', 163, 149, self.fmt.type) + struct.pack(self.
        fmt.msg_struct, *values)