def plot_meshes(self, ax=None, marker='+', color='blue', outlines=False, **
    kwargs):
    import matplotlib.pyplot as plt
    kwargs['color'] = color
    if ax is None:
        ax = plt.gca()
    ax.scatter(self.x, self.y, marker=marker, color=color)
    if outlines:
        from ..aperture import RectangularAperture
        xy = np.column_stack([self.x, self.y])
        apers = RectangularAperture(xy, self.box_size[1], self.box_size[0], 0.0
            )
        apers.plot(ax=ax, **kwargs)
    return