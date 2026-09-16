def line_point_(self, label=None, style=None, opts=None, options={}, colors
    ={'line': 'orange', 'point': '#30A2DA'}):
    try:
        if style is None:
            style = self.chart_style
            if 'size' not in style:
                style['size'] = 10
        style['color'] = colors['line']
        c = self._get_chart('line', style=style, opts=opts, label=label,
            options=options)
        style['color'] = colors['point']
        c2 = self._get_chart('point', style=style, opts=opts, label=label,
            options=options)
        return c * c2
    except Exception as e:
        self.err(e, self.line_point_, 'Can not draw line_point chart')