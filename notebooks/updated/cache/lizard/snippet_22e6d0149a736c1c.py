def share(self, base=None, keys=None, by=None, **kwargs):
    if by is not None:
        if base is not None:
            if hasattr(base, 'psy') or isinstance(base, Plotter):
                base = [base]
            if by.lower() in ['ax', 'axes']:
                bases = {ax: p[0] for ax, p in six.iteritems(Project(base).
                    axes)}
            elif by.lower() in ['fig', 'figure']:
                bases = {fig: p[0] for fig, p in six.iteritems(Project(base
                    ).figs)}
            else:
                raise ValueError(
                    "*by* must be out of {'fig', 'figure', 'ax', 'axes'}. Not %s"
                     % (by,))
        else:
            bases = {}
        projects = self.axes if by == 'axes' else self.figs
        for obj, p in projects.items():
            p.share(bases.get(obj), keys, **kwargs)
    else:
        plotters = self.plotters
        if not plotters:
            return
        if base is None:
            if len(plotters) == 1:
                return
            base = plotters[0]
            plotters = plotters[1:]
        elif not isinstance(base, Plotter):
            base = getattr(getattr(base, 'psy', base), 'plotter', base)
        base.share(plotters, keys=keys, **kwargs)