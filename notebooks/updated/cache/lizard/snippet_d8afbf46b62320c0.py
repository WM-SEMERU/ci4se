def asFloat(self, maxval=1.0):
    x, y, pixels, info = self.asDirect()
    sourcemaxval = 2 ** info['bitdepth'] - 1
    del info['bitdepth']
    info['maxval'] = float(maxval)
    factor = float(maxval) / float(sourcemaxval)

    def iterfloat():
        for row in pixels:
            yield map(factor.__mul__, row)
    return x, y, iterfloat(), info