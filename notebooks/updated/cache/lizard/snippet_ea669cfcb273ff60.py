def get_ax_fig_plt(ax=None, **kwargs):
    import matplotlib.pyplot as plt
    if ax is None:
        fig = plt.figure(**kwargs)
        ax = fig.add_subplot(1, 1, 1)
    else:
        fig = plt.gcf()
    return ax, fig, plt