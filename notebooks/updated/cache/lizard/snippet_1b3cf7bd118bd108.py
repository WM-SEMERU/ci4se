def enum(self, other, rmax, process=None, bunch=100000, **kwargs):
    rall = None
    if process is None:
        rall = [numpy.empty(0, 'f8')]
        iall = [numpy.empty(0, 'intp')]
        jall = [numpy.empty(0, 'intp')]

        def process(r1, i1, j1, **kwargs):
            rall[0] = numpy.append(rall[0], r1)
            iall[0] = numpy.append(iall[0], i1)
            jall[0] = numpy.append(jall[0], j1)
    _core.KDNode.enum(self, other, rmax, process, bunch, **kwargs)
    if rall is not None:
        return rall[0], iall[0], jall[0]
    else:
        return None