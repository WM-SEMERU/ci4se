def calendarplot(data, how='sum', yearlabels=True, yearascending=True,
    yearlabel_kws=None, subplot_kws=None, gridspec_kws=None, fig_kws=None,
    **kwargs):
    yearlabel_kws = yearlabel_kws or {}
    subplot_kws = subplot_kws or {}
    gridspec_kws = gridspec_kws or {}
    fig_kws = fig_kws or {}
    years = np.unique(data.index.year)
    if not yearascending:
        years = years[::-1]
    fig, axes = plt.subplots(nrows=len(years), ncols=1, squeeze=False,
        subplot_kw=subplot_kws, gridspec_kw=gridspec_kws, **fig_kws)
    axes = axes.T[0]
    if how is None:
        by_day = data
    elif _pandas_18:
        by_day = data.resample('D').agg(how)
    else:
        by_day = data.resample('D', how=how)
    ylabel_kws = dict(fontsize=32, color=kwargs.get('fillcolor',
        'whitesmoke'), fontweight='bold', fontname='Arial', ha='center')
    ylabel_kws.update(yearlabel_kws)
    max_weeks = 0
    for year, ax in zip(years, axes):
        yearplot(by_day, year=year, how=None, ax=ax, **kwargs)
        max_weeks = max(max_weeks, ax.get_xlim()[1])
        if yearlabels:
            ax.set_ylabel(str(year), **ylabel_kws)
    for ax in axes:
        ax.set_xlim(0, max_weeks)
    plt.tight_layout()
    return fig, axes