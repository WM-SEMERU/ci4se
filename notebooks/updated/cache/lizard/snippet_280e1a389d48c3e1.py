def funnel(self, serie):
    serie_node = self.svg.serie(serie)
    fmt = lambda x: '%f %f' % x
    for i, poly in enumerate(serie.points):
        metadata = serie.metadata.get(i)
        val = self._format(serie, i)
        funnels = decorate(self.svg, self.svg.node(serie_node['plot'],
            class_='funnels'), metadata)
        alter(self.svg.node(funnels, 'polygon', points=' '.join(map(fmt,
            map(self.view, poly))), class_=
            'funnel reactive tooltip-trigger'), metadata)
        x, y = self.view((self._center(self._x_pos[serie.index]), sum([
            point[1] for point in poly]) / len(poly)))
        self._tooltip_data(funnels, val, x, y, 'centered', self.
            _get_x_label(serie.index))
        self._static_value(serie_node, val, x, y, metadata)