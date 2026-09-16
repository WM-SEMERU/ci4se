def lasso_leftdown(self, event=None):
    try:
        self.report_leftdown(event=event)
    except:
        return
    if event.inaxes:
        color = 'goldenrod'
        cmap = getattr(self.conf, 'cmap', None)
        if isinstance(cmap, dict):
            cmap = cmap['int']
        try:
            if cmap is not None:
                rgb = (int(i * 255) ^ 255 for i in cmap._lut[0][:3])
                color = '#%02x%02x%02x' % tuple(rgb)
        except:
            pass
        self.lasso = Lasso(event.inaxes, (event.xdata, event.ydata), self.
            lassoHandler)
        self.lasso.line.set_color(color)