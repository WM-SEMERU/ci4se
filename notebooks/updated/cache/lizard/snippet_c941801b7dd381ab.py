def single(self, trigs):
    newsnr = ranking.get_newsnr(trigs)
    rchisq = trigs['chisq'][:] / (2.0 * trigs['chisq_dof'][:] - 2.0)
    newsnr[numpy.logical_and(newsnr < 10, rchisq > 2)] = -1
    return newsnr