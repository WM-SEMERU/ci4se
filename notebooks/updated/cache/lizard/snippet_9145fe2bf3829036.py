def _init(self):
    if self.num_samples:
        assert len(self.realizations) == self.num_samples, (len(self.
            realizations), self.num_samples)
        for rlz in self.realizations:
            for k in rlz.weight.dic:
                rlz.weight.dic[k] = 1.0 / self.num_samples
    else:
        tot_weight = sum(rlz.weight for rlz in self.realizations)
        if not tot_weight.is_one():
            for rlz in self.realizations:
                rlz.weight = rlz.weight / tot_weight