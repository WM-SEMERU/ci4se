def _strslices(self):
    pad = self.padding or 0
    for sli in self.slices():
        if sli.start + 1 == sli.stop:
            yield '%0*d' % (pad, sli.start)
        else:
            assert sli.step >= 0, 'Internal error: sli.step < 0'
            if sli.step == 1:
                yield '%0*d-%0*d' % (pad, sli.start, pad, sli.stop - 1)
            else:
                yield '%0*d-%0*d/%d' % (pad, sli.start, pad, sli.stop - 1,
                    sli.step)