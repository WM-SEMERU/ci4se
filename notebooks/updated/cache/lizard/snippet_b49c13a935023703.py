def plot(self, series, label='', color=None, style=None):
    color = self.get_color(color)
    if self.stacked:
        series += self.running_sum
        plt.fill_between(series.index, self.running_sum, series, facecolor=
            ALPHAS[color])
        self.running_sum = series
        plt.gca().set_ylim(bottom=0, top=int(series.max() * 1.05))
    series.plot(label=label, c=COLORS[color], linewidth=2, style=style)