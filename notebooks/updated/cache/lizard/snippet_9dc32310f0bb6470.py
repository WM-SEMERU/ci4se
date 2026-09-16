def plot_fixed_x(self, x_values, x_derivative=0, steps=1000, smooth=0,
    simple='auto', ymin='auto', ymax='auto', format=True, clear=1):
    if simple == 'auto':
        simple = self.simple
    if ymin == 'auto':
        ymin = self.ymin
    if ymax == 'auto':
        ymax = self.ymax
    if clear:
        _pylab.gca().clear()
    if not type(x_values) in [type([]), type(_pylab.array([]))]:
        x_values = [x_values]
    for x in x_values:

        def f(y):
            return self.evaluate(x, y, x_derivative, smooth, simple)
        _pylab_help.plot_function(f, ymin, ymax, steps, 0, False)
        a = _pylab.gca()
        a.set_xlabel(self.ylabel)
        if x_derivative:
            a.set_ylabel(str(x_derivative) + ' ' + str(self.xlabel) +
                ' derivative of ' + self.zlabel)
        else:
            a.set_ylabel(self.zlabel)
        a.set_title(self._path + '\nSpline array plot at fixed x = ' + self
            .xlabel)
        a.get_lines()[-1].set_label('x (' + self.xlabel + ') = ' + str(x))
    if format:
        _s.format_figure()
    return a