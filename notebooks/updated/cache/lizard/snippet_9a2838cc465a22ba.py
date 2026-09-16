def save_all_figures_todir(self, dirname):
    fignames = []
    for thumbnail in self._thumbnails:
        fig = thumbnail.canvas.fig
        fmt = thumbnail.canvas.fmt
        fext = {'image/png': '.png', 'image/jpeg': '.jpg', 'image/svg+xml':
            '.svg'}[fmt]
        figname = get_unique_figname(dirname, 'Figure', fext)
        save_figure_tofile(fig, fmt, figname)
        fignames.append(figname)
    return fignames