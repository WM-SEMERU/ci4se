def needle(self, serie):
    serie_node = self.svg.serie(serie)
    for i, theta in enumerate(serie.values):
        if theta is None:
            continue

        def point(x, y):
            return '%f %f' % self.view((x, y))
        val = self._format(serie, i)
        metadata = serie.metadata.get(i)
        gauges = decorate(self.svg, self.svg.node(serie_node['plot'],
            class_='dots'), metadata)
        tolerance = 1.15
        if theta < self._min:
            theta = self._min * tolerance
        if theta > self._max:
            theta = self._max * tolerance
        w = (self._box._tmax - self._box._tmin + self.view.aperture) / 4
        if self.logarithmic:
            w = min(w, self._min - self._min * 10 ** -10)
        alter(self.svg.node(gauges, 'path', d='M %s L %s A %s 1 0 1 %s Z' %
            (point(0.85, theta), point(self.needle_width, theta - w), 
            '%f %f' % (self.needle_width, self.needle_width), point(self.
            needle_width, theta + w)), class_=
            'line reactive tooltip-trigger'), metadata)
        x, y = self.view((0.75, theta))
        self._tooltip_data(gauges, val, x, y, xlabel=self._get_x_label(i))
        self._static_value(serie_node, val, x, y, metadata)