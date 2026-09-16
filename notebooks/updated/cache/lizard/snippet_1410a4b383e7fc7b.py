def plot_gaps(plot, columns):
    from plot_window import window_plot_convolve as plot_window
    plot_window([[(100 - i) for i in columns]], len(columns) * 0.01, plot)