def plot_roc(evaluation, class_index=None, title=None, key_loc=
    'lower right', outfile=None, wait=True):
    if not plot.matplotlib_available:
        logger.error('Matplotlib is not installed, plotting unavailable!')
        return
    if class_index is None:
        class_index = [0]
    ax = None
    for cindex in class_index:
        data = generate_thresholdcurve_data(evaluation, cindex)
        head = evaluation.header
        area = get_auc(data)
        x, y = get_thresholdcurve_data(data, 'False Positive Rate',
            'True Positive Rate')
        if ax is None:
            fig, ax = plt.subplots()
            ax.set_xlabel('False Positive Rate')
            ax.set_ylabel('True Positive Rate')
            if title is None:
                title = 'ROC'
            ax.set_title(title)
            ax.grid(True)
            fig.canvas.set_window_title(title)
            plt.xlim([-0.05, 1.05])
            plt.ylim([-0.05, 1.05])
        plot_label = head.class_attribute.value(cindex
            ) + ' (AUC: %0.4f)' % area
        ax.plot(x, y, label=plot_label)
        ax.plot(ax.get_xlim(), ax.get_ylim(), ls='--', c='0.3')
    plt.draw()
    plt.legend(loc=key_loc, shadow=True)
    if outfile is not None:
        plt.savefig(outfile)
    if wait:
        plt.show()