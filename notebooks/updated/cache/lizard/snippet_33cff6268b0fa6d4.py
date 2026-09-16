def plot_lines(it):
    data = [go.Scatter(mode='lines', **d) for d in it]
    return py.iplot(data, filename='scatter-mode')