def plot_discrete(self, show=False, annotations=True):
    import matplotlib.pyplot as plt
    axis = plt.axes()
    axis.set_aspect('equal', 'datalim')
    for i, points in enumerate(self.discrete):
        color = ['g', 'k'][i in self.root]
        axis.plot(*points.T, color=color)
    if annotations:
        for e in self.entities:
            if not hasattr(e, 'plot'):
                continue
            e.plot(self.vertices)
    if show:
        plt.show()
    return axis