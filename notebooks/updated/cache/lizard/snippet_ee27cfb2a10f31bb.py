def write_frame(self, buf):
    writer = Writer(buf)
    writer.write_octet(self.type())
    writer.write_short(self.channel_id)
    stream_args_len_pos = len(buf)
    writer.write_long(0)
    stream_method_pos = len(buf)
    writer.write_short(self._class_id)
    writer.write_short(self._weight)
    writer.write_longlong(self._size)
    if self.DEFAULT_PROPERTIES:
        flags_pos = len(buf)
        writer.write_short(0)
        flag_bits = 0
        for key, proptype, rfunc, wfunc, mask in self.PROPERTIES:
            val = self._properties.get(key, None)
            if val is not None:
                flag_bits |= mask
                wfunc(writer, val)
        writer.write_short_at(flag_bits, flags_pos)
    else:
        shift = 15
        flag_bits = 0
        flags = []
        stack = deque()
        for key, proptype, rfunc, wfunc, mask in self.PROPERTIES:
            val = self._properties.get(key, None)
            if val is not None:
                if shift == 0:
                    flags.append(flag_bits)
                    flag_bits = 0
                    shift = 15
                flag_bits |= 1 << shift
                stack.append((wfunc, val))
            shift -= 1
        flags.append(flag_bits)
        for flag_bits in flags:
            writer.write_short(flag_bits)
        for method, val in stack:
            method(writer, val)
    stream_len = len(buf) - stream_method_pos
    writer.write_long_at(stream_len, stream_args_len_pos)
    writer.write_octet(206)