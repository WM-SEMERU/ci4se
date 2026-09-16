def get_mean(self, grp=None):
    self.init()
    if len(self.weights) == 1:
        pmap = self.get(0, grp)
        for sid, pcurve in pmap.items():
            array = numpy.zeros(pcurve.array.shape[:-1] + (2,))
            array[:, (0)] = pcurve.array[:, (0)]
            pcurve.array = array
        return pmap
    else:
        dic = {g: self.dstore['poes/' + g] for g in self.dstore['poes']
            } if grp is None else {grp: self.dstore['poes/' + grp]}
        pmaps = self.rlzs_assoc.combine_pmaps(dic)
        return stats.compute_pmap_stats(pmaps, [stats.mean_curve, stats.
            std_curve], self.weights, self.imtls)