def to_wire(self, file=None, compress=None, origin=None):
    if file is None:
        file = cStringIO.StringIO()
        want_return = True
    else:
        want_return = False
    if not self.is_absolute():
        if origin is None or not origin.is_absolute():
            raise NeedAbsoluteNameOrOrigin
        labels = list(self.labels)
        labels.extend(list(origin.labels))
    else:
        labels = self.labels
    i = 0
    for label in labels:
        n = Name(labels[i:])
        i += 1
        if not compress is None:
            pos = compress.get(n)
        else:
            pos = None
        if not pos is None:
            value = 49152 + pos
            s = struct.pack('!H', value)
            file.write(s)
            break
        else:
            if not compress is None and len(n) > 1:
                pos = file.tell()
                if pos < 49152:
                    compress[n] = pos
            l = len(label)
            file.write(chr(l))
            if l > 0:
                file.write(label)
    if want_return:
        return file.getvalue()