def check(self, triggers, data_reader):
    if len(triggers['snr']) == 0:
        return None
    i = triggers['snr'].argmax()
    rchisq = triggers['chisq'][i]
    nsnr = ranking.newsnr(triggers['snr'][i], rchisq)
    dur = triggers['template_duration'][i]
    if (nsnr > self.newsnr_threshold and rchisq < self.
        reduced_chisq_threshold and dur > self.duration_threshold):
        fake_coinc = {('foreground/%s/%s' % (self.ifo, k)): triggers[k][i] for
            k in triggers}
        fake_coinc['foreground/stat'] = nsnr
        fake_coinc['foreground/ifar'] = self.fixed_ifar
        fake_coinc['HWINJ'] = data_reader.near_hwinj()
        return fake_coinc
    return None