def plot_depth_histogram(catalogue, bin_width, normalisation=False,
    bootstrap=None, filename=None, figure_size=(8, 6), filetype='png', dpi=
    300, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=figure_size)
    else:
        fig = ax.get_figure()
    if len(catalogue.data['depth']) == 0:
        raise ValueError('No depths reported in catalogue!')
    depth_bins = np.arange(0.0, np.max(catalogue.data['depth']) + bin_width,
        bin_width)
    depth_hist = catalogue.get_depth_distribution(depth_bins, normalisation,
        bootstrap)
    ax.bar(depth_bins[:-1], depth_hist, width=0.95 * bin_width, edgecolor='k')
    ax.set_xlabel('Depth (km)')
    if normalisation:
        ax.set_ylabel('Probability Mass Function')
    else:
        ax.set_ylabel('Count')
    ax.set_title('Depth Histogram')
    _save_image(fig, filename, filetype, dpi)