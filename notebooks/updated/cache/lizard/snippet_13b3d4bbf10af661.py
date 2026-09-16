def knob_subgroup(self, cutoff=7.0):
    if cutoff > self.cutoff:
        raise ValueError(
            'cutoff supplied ({0}) cannot be greater than self.cutoff ({1})'
            .format(cutoff, self.cutoff))
    return KnobGroup(monomers=[x for x in self.get_monomers() if x.
        max_kh_distance <= cutoff], ampal_parent=self.ampal_parent)