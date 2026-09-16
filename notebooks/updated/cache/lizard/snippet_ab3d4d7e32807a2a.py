def _get_str_range(self, vals_stats):
    minmax = vals_stats[1]
    minval = self.fmtstr.format(minmax[0])
    maxval = self.fmtstr.format(minmax[1])
    return '{A} to {B:6>}'.format(A=minval, B=maxval)