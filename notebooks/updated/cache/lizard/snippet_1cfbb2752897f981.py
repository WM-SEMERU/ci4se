def contour(c, subsample=1, size=10, color='g'):
    if not isinstance(c, Contour):
        raise ValueError('Input must be of type Contour')
    for i in range(c.num_pixels)[0::subsample]:
        plt.scatter(c.boundary_pixels[i, 1], c.boundary_pixels[i, 0], s=
            size, c=color)