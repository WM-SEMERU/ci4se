def plot_sfs_folded(*args, **kwargs):
    ax = plot_sfs(*args, **kwargs)
    n = kwargs.get('n', None)
    if n:
        ax.set_xlabel('minor allele frequency')
    else:
        ax.set_xlabel('minor allele count')
    return ax