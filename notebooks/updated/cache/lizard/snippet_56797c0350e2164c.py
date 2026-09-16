def single(self, trigs):
    chisq_newsnr = ranking.get_newsnr(trigs)
    rautochisq = trigs['cont_chisq'][:] / trigs['cont_chisq_dof'][:]
    autochisq_newsnr = ranking.newsnr(trigs['snr'][:], rautochisq)
    return numpy.array(numpy.minimum(chisq_newsnr, autochisq_newsnr, dtype=
        numpy.float32), ndmin=1, copy=False)