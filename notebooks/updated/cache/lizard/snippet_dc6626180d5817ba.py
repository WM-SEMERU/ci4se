def plot_polygon(polygon, show=True, **kwargs):
    import matplotlib.pyplot as plt

    def plot_single(single):
        plt.plot(*single.exterior.xy, **kwargs)
        for interior in single.interiors:
            plt.plot(*interior.xy, **kwargs)
    plt.axes().set_aspect('equal', 'datalim')
    if util.is_sequence(polygon):
        [plot_single(i) for i in polygon]
    else:
        plot_single(polygon)
    if show:
        plt.show()