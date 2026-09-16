def transform(self):
    ax = self.ax
    return {'axes': ax.transAxes, 'fig': ax.get_figure().transFigure,
        'data': ax.transData}