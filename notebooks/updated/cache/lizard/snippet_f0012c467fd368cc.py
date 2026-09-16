def save_cb(self):
    w = Widgets.SaveDialog(title='Save plot')
    target = w.get_path()
    if target is None:
        return
    plot_ext = self.settings.get('file_suffix', '.png')
    if not target.endswith(plot_ext):
        target += plot_ext
    fig_dpi = 100
    try:
        fig = self.tab_plot.get_figure()
        fig.savefig(target, dpi=fig_dpi)
    except Exception as e:
        self.logger.error(str(e))
    else:
        self.logger.info('Table plot saved as {0}'.format(target))