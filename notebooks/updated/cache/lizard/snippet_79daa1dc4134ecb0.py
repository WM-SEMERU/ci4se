def create_multiple_bar_chart(self, x_labels, mul_y_values, mul_y_labels,
    normalize=False):
    self.setup(0.25)
    ax1 = self.get_ax()
    ax1.set_xticks(list(range(len(x_labels))))
    ax1.set_xticklabels([x_labels[i] for i in range(len(x_labels))],
        rotation=90)
    y_counts = len(mul_y_values)
    colors = cm.rainbow(np.linspace(0, 1, y_counts))
    max_bar_width = 0.6
    bar_width = max_bar_width / y_counts
    x_shifts = np.linspace(0, max_bar_width, y_counts) - max_bar_width * 0.5
    ax_series = []
    for i in range(y_counts):
        x_pos = range(len(x_labels))
        x_pos = np.array(x_pos) + x_shifts[i]
        if normalize:
            y_values = normalize_array(mul_y_values[i])
        else:
            y_values = mul_y_values[i]
        ax_series.append(ax1.bar(x_pos, y_values, width=bar_width, align=
            'center', color=colors[i]))
    ax1.legend(ax_series, mul_y_labels)
    return ax1