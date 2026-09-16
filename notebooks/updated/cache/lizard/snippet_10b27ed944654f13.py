def calc_point_distance_vary(self, chi_coords, point_fupper, mus):
    chi1_bin, chi2_bin = self.find_point_bin(chi_coords)
    min_dist = 1000000000
    indexes = None
    for chi1_bin_offset, chi2_bin_offset in self.bin_loop_order:
        curr_chi1_bin = chi1_bin + chi1_bin_offset
        curr_chi2_bin = chi2_bin + chi2_bin_offset
        curr_bank = self.massbank[curr_chi1_bin][curr_chi2_bin]
        if not curr_bank['mass1s'].size:
            continue
        f_upper = numpy.minimum(point_fupper, curr_bank['freqcuts'])
        f_other = numpy.maximum(point_fupper, curr_bank['freqcuts'])
        freq_idxes = numpy.array([self.frequency_map[f] for f in f_upper])
        vecs1 = mus[(freq_idxes), :]
        range_idxes = numpy.arange(len(freq_idxes))
        vecs2 = curr_bank['mus'][(range_idxes), (freq_idxes), :]
        dists = (vecs1 - vecs2) * (vecs1 - vecs2)
        dists = numpy.sum(dists, axis=1)
        norm_upper = numpy.array([self.normalization_map[f] for f in f_upper])
        norm_other = numpy.array([self.normalization_map[f] for f in f_other])
        norm_fac = norm_upper / norm_other
        renormed_dists = 1 - (1 - dists) * norm_fac
        curr_min_dist = renormed_dists.min()
        if curr_min_dist < min_dist:
            min_dist = curr_min_dist
            indexes = curr_chi1_bin, curr_chi2_bin, renormed_dists.argmin()
    return min_dist, indexes