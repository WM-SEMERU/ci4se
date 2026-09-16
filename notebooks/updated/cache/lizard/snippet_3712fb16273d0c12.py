def _set_pyqtgraph_title(layout):
    if 'title_size' in pytplot.tplot_opt_glob:
        size = pytplot.tplot_opt_glob['title_size']
    if 'title_text' in pytplot.tplot_opt_glob:
        if pytplot.tplot_opt_glob['title_text'] != '':
            layout.addItem(LabelItem(pytplot.tplot_opt_glob['title_text'],
                size=size, color='k'), row=0, col=0)
            return True
    return False