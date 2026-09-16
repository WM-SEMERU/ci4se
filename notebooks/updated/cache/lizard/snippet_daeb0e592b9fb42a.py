def adjust_strain(self, strain, delta_fs=None, delta_qinv=None, delta_fc=
    None, kappa_c=1.0, kappa_tst_re=1.0, kappa_tst_im=0.0, kappa_pu_re=1.0,
    kappa_pu_im=0.0):
    fc = self.fc0 + delta_fc if delta_fc else self.fc0
    fs = self.fs0 + delta_fs if delta_fs else self.fs0
    qinv = self.qinv0 + delta_qinv if delta_qinv else self.qinv0
    r_adjusted = self.update_r(fs=fs, qinv=qinv, fc=fc, kappa_c=kappa_c,
        kappa_tst_re=kappa_tst_re, kappa_tst_im=kappa_tst_im, kappa_pu_re=
        kappa_pu_re, kappa_pu_im=kappa_pu_im)
    k = r_adjusted / self.r0
    k_amp = np.abs(k)
    k_phase = np.unwrap(np.angle(k))
    order = 1
    k_amp_off = UnivariateSpline(self.freq, k_amp, k=order, s=0)
    k_phase_off = UnivariateSpline(self.freq, k_phase, k=order, s=0)
    freq_even = strain.sample_frequencies.numpy()
    k_even_sample = k_amp_off(freq_even) * np.exp(1.0j * k_phase_off(freq_even)
        )
    strain_adjusted = FrequencySeries(strain.numpy() * k_even_sample,
        delta_f=strain.delta_f)
    return strain_adjusted