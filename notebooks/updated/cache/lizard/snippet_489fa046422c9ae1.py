def plot_loglogs(cls, loc=None, iloc=None, show_censors=False,
    censor_styles=None, **kwargs):

    def loglog(s):
        return np.log(-np.log(s))
    if loc is not None and iloc is not None:
        raise ValueError('Cannot set both loc and iloc in call to .plot().')
    if censor_styles is None:
        censor_styles = {}
    set_kwargs_ax(kwargs)
    set_kwargs_color(kwargs)
    set_kwargs_drawstyle(kwargs)
    kwargs['logx'] = True
    dataframe_slicer = create_dataframe_slicer(iloc, loc)
    ax = kwargs['ax']
    colour = kwargs['c']
    if show_censors and cls.event_table['censored'].sum() > 0:
        cs = {'marker': '+', 'ms': 12, 'mew': 1}
        cs.update(censor_styles)
        times = dataframe_slicer(cls.event_table.loc[cls.event_table[
            'censored'] > 0]).index.values.astype(float)
        v = cls.predict(times)
        ax.plot(times, loglog(v), linestyle='None', color=colour, **cs)
    dataframe_slicer(loglog(cls.survival_function_)).plot(**kwargs)
    ax.set_xlabel('log(timeline)')
    ax.set_ylabel('log(-log(survival_function_))')
    return ax