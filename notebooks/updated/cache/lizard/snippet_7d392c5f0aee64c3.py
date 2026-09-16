def set_n_nlmo(self):
    nnlmo = 0
    data_tmp = self.data
    data_tmp.pop('lmax')
    data_tmp.pop('n_nlo')
    data_tmp.pop('preamble')
    for l_zeta_ng in data_tmp:
        l = l_zeta_ng.split('_')[0]
        nnlmo = nnlmo + (2 * int(l) + 1)
    return str(nnlmo)