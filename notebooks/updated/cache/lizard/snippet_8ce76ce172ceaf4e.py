def _extract_nn_info(self, structure, nns):
    if self.targets is None:
        targets = structure.composition.elements
    else:
        targets = self.targets
    siw = []
    max_weight = max(nn[self.weight] for nn in nns.values())
    for nstats in nns.values():
        site = nstats['site']
        if nstats[self.weight] > self.tol * max_weight and self._is_in_targets(
            site, targets):
            nn_info = {'site': site, 'image': self._get_image(structure,
                site), 'weight': nstats[self.weight] / max_weight,
                'site_index': self._get_original_site(structure, site)}
            if self.extra_nn_info:
                poly_info = nstats
                del poly_info['site']
                nn_info['poly_info'] = poly_info
            siw.append(nn_info)
    return siw