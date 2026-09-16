def ximshow_rectified(self, slitlet2d_rect):
    title = 'Slitlet#' + str(self.islitlet) + ' (rectify)'
    ax = ximshow(slitlet2d_rect, title=title, first_pixel=(self.bb_nc1_orig,
        self.bb_ns1_orig), show=False)
    xx = np.arange(0, self.bb_nc2_orig - self.bb_nc1_orig + 1, dtype=np.float)
    for spectrail in self.list_spectrails:
        yy0 = self.corr_yrect_a + self.corr_yrect_b * spectrail(self.
            x0_reference)
        yy = np.tile([yy0 - self.bb_ns1_orig], xx.size)
        ax.plot(xx + self.bb_nc1_orig, yy + self.bb_ns1_orig, 'b')
    for spectrail in self.list_frontiers:
        yy0 = self.corr_yrect_a + self.corr_yrect_b * spectrail(self.
            x0_reference)
        yy = np.tile([yy0 - self.bb_ns1_orig], xx.size)
        ax.plot(xx + self.bb_nc1_orig, yy + self.bb_ns1_orig, 'b:')
    pause_debugplot(self.debugplot, pltshow=True)