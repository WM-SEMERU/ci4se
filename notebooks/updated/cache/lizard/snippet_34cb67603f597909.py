def setScales(self, scales=None, term_num=None):
    if scales == None:
        for term_i in range(self.n_terms):
            n_scales = self.vd.getTerm(term_i).getNumberScales()
            self.vd.getTerm(term_i).setScales(SP.array(SP.randn(n_scales)))
    elif term_num == None:
        assert scales.shape[0] == self.vd.getNumberScales(
            ), 'incompatible shape'
        index = 0
        for term_i in range(self.n_terms):
            index1 = index + self.vd.getTerm(term_i).getNumberScales()
            self.vd.getTerm(term_i).setScales(scales[index:index1])
            index = index1
    else:
        assert scales.shape[0] == self.vd.getTerm(term_num).getNumberScales(
            ), 'incompatible shape'
        self.vd.getTerm(term_num).setScales(scales)