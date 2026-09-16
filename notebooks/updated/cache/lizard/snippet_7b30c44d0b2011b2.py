def nodeDumpOutput(self, buf, cur, level, format, encoding):
    if buf is None:
        buf__o = None
    else:
        buf__o = buf._o
    if cur is None:
        cur__o = None
    else:
        cur__o = cur._o
    libxml2mod.xmlNodeDumpOutput(buf__o, self._o, cur__o, level, format,
        encoding)