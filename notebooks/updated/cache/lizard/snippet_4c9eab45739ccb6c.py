def get_shiftfile_row(self):
    if self.fit is not None:
        rowstr = '%s    %0.6f  %0.6f    %0.6f     %0.6f   %0.6f  %0.6f\n' % (
            self.name, self.fit['offset'][0], self.fit['offset'][1], self.
            fit['rot'], self.fit['scale'][0], self.fit['rms'][0], self.fit[
            'rms'][1])
    else:
        rowstr = None
    return rowstr