def wrplt(self, fout_dir, plt_ext='png'):
    basename = self.grprobj.get_fout_base(self.ntplt.hdrgo)
    plt_pat = self.get_pltpat(plt_ext)
    fout_basename = plt_pat.format(BASE=basename)
    fout_plt = os.path.join(fout_dir, fout_basename)
    self.gosubdagplot.plt_dag(fout_plt)
    return fout_plt