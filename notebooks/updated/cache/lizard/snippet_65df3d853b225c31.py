def dotted(self):
    if self._dotted is None:
        output = []
        part = 0
        for byte in self.contents:
            if _PY2:
                byte = ord(byte)
            part = part * 128
            part += byte & 127
            if byte & 128 == 0:
                if len(output) == 0:
                    output.append(str_cls(part // 40))
                    output.append(str_cls(part % 40))
                else:
                    output.append(str_cls(part))
                part = 0
        self._dotted = '.'.join(output)
    return self._dotted