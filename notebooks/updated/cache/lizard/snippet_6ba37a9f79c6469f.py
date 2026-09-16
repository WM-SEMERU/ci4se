def plot_brillouin(self):
    labels = {}
    for q in self._bs.qpoints:
        if q.label:
            labels[q.label] = q.frac_coords
    lines = []
    for b in self._bs.branches:
        lines.append([self._bs.qpoints[b['start_index']].frac_coords, self.
            _bs.qpoints[b['end_index']].frac_coords])
    plot_brillouin_zone(self._bs.lattice_rec, lines=lines, labels=labels)