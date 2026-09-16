def array_scanlines_interlace(self, pixels):
    fmt = 'BH'[self.bitdepth > 8]
    vpr = self.width * self.planes
    for lines in adam7_generate(self.width, self.height):
        for x, y, xstep in lines:
            ppr = int(math.ceil((self.width - x) / float(xstep)))
            reduced_row_len = ppr * self.planes
            if xstep == 1:
                offset = y * vpr
                yield pixels[offset:offset + vpr]
                continue
            row = array(fmt)
            row.extend(pixels[0:reduced_row_len])
            offset = y * vpr + x * self.planes
            end_offset = (y + 1) * vpr
            skip = self.planes * xstep
            for i in range(self.planes):
                row[i::self.planes] = pixels[offset + i:end_offset:skip]
            yield row