def _lsm_fix_strip_offsets(self):
    if self.filehandle.size < 2 ** 32:
        return
    pages = self.pages
    npages = len(pages)
    series = self.series[0]
    axes = series.axes
    positions = 1
    for i in (0, 1):
        if series.axes[i] in 'PM':
            positions *= series.shape[i]
    if positions > 1:
        ntimes = 0
        for i in (1, 2):
            if axes[i] == 'T':
                ntimes = series.shape[i]
                break
        if ntimes:
            div, mod = divmod(npages, 2 * positions * ntimes)
            assert mod == 0
            shape = positions, ntimes, div, 2
            indices = numpy.arange(product(shape)).reshape(shape)
            indices = numpy.moveaxis(indices, 1, 0)
    else:
        indices = numpy.arange(npages).reshape(-1, 2)
    if pages[0]._offsetscounts[0][0] > pages[1]._offsetscounts[0][0]:
        indices = indices[(...), ::-1]
    wrap = 0
    previousoffset = 0
    for i in indices.flat:
        page = pages[int(i)]
        dataoffsets = []
        for currentoffset in page._offsetscounts[0]:
            if currentoffset < previousoffset:
                wrap += 2 ** 32
            dataoffsets.append(currentoffset + wrap)
            previousoffset = currentoffset
        page._offsetscounts = dataoffsets, page._offsetscounts[1]