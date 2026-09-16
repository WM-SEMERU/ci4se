def __write_palette(self, outfile):
    p = bytearray()
    t = bytearray()
    for x in self.palette:
        p.extend(x[0:3])
        if len(x) > 3:
            t.append(x[3])
    write_chunk(outfile, 'PLTE', bytearray_to_bytes(p))
    if t:
        write_chunk(outfile, 'tRNS', bytearray_to_bytes(t))