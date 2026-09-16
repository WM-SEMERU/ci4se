def pauling_stability_ratio(self):
    if self._pauling_stability_ratio is None:
        if self.ce_symbol in ['S:1', 'L:2']:
            self._pauling_stability_ratio = 0.0
        else:
            mindist_anions = 1000000.0
            mindist_cation_anion = 1000000.0
            for ipt1 in range(len(self.points)):
                pt1 = np.array(self.points[ipt1])
                mindist_cation_anion = min(mindist_cation_anion, np.linalg.
                    norm(pt1 - self.central_site))
                for ipt2 in range(ipt1 + 1, len(self.points)):
                    pt2 = np.array(self.points[ipt2])
                    mindist_anions = min(mindist_anions, np.linalg.norm(pt1 -
                        pt2))
            anion_radius = mindist_anions / 2.0
            cation_radius = mindist_cation_anion - anion_radius
            self._pauling_stability_ratio = cation_radius / anion_radius
    return self._pauling_stability_ratio