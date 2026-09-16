def stylesheet(self, fn=None, unit=CSS.rem, pt_per_em=None, decimals=2,
    font_factor=1 / 2.0, space_factor=1 / 20.0):
    styles = self.stylemap(definitions=True, all=True, cache=False)
    used_styles = self.stylemap(definitions=False, all=False, cache=False)
    css = CSS(fn=fn or self.fn and self.fn.replace('.docx', '.css') or None)
    if pt_per_em is None:
        normal = [styles[k] for k in styles if styles[k].name == 'Normal'][0]
        if normal.properties.get('sz') is not None:
            pt_per_em = float(normal.properties['sz'].val) * font_factor
        else:
            pt_per_em = 12.0
    for styleName in used_styles:
        style = styles[styleName]
        sel = self.selector(style)
        css.styles[sel] = self.style_properties(styles, styleName, unit=
            unit, pt_per_em=pt_per_em, decimals=decimals, font_factor=
            font_factor, space_factor=space_factor)
        LOG.debug('%s %r' % (sel, css.styles[sel]))
    return css