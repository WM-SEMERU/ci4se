def _repr_html_(self):
    if self.size < 10:
        return np.ndarray.__repr__(self)
    attribs = self.__dict__.copy()
    row1 = '<tr><th style="text-align:center;" colspan="2">{} [{{}}]</th></tr>'
    rows = row1.format(attribs.pop('mnemonic'))
    rows = rows.format(attribs.pop('units', '&ndash;'))
    row2 = (
        '<tr><td style="text-align:center;" colspan="2">{:.4f} : {:.4f} : {:.4f}</td></tr>'
        )
    rows += row2.format(attribs.pop('start'), self.stop, attribs.pop('step'))
    s = '<tr><td><strong>{k}</strong></td><td>{v}</td></tr>'
    for k, v in attribs.items():
        rows += s.format(k=k, v=v)
    rows += (
        '<tr><th style="border-top: 2px solid #000; text-align:center;" colspan="2"><strong>Stats</strong></th></tr>'
        )
    stats = self.get_stats()
    s = (
        '<tr><td><strong>samples (NaNs)</strong></td><td>{samples} ({nulls})</td></tr>'
        )
    s += '<tr><td><strong><sub>min</sub> mean <sup>max</sup></strong></td>'
    s += '<td><sub>{min:.2f}</sub> {mean:.3f} <sup>{max:.2f}</sup></td></tr>'
    rows += s.format(**stats)
    s = (
        '<tr><th style="border-top: 2px solid #000;">Depth</th><th style="border-top: 2px solid #000;">Value</th></tr>'
        )
    rows += s.format(self.start, self[0])
    s = '<tr><td>{:.4f}</td><td>{:.4f}</td></tr>'
    for depth, value in zip(self.basis[:3], self[:3]):
        rows += s.format(depth, value)
    rows += '<tr><td>⋮</td><td>⋮</td></tr>'
    for depth, value in zip(self.basis[-3:], self[-3:]):
        rows += s.format(depth, value)
    html = '<table>{}</table>'.format(rows)
    return html