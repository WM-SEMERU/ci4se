def saveplot(fig, *name_args, close=True, **name_kwargs):
    oname = out_name(*name_args, **name_kwargs)
    fig.savefig('{}.{}'.format(oname, conf.plot.format), format=conf.plot.
        format, bbox_inches='tight')
    if close:
        plt.close(fig)