def plot(self, numPoints=100):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-self.radius, self.radius, numPoints)
    z = np.linspace(-self.height / 2.0, self.height / 2.0, numPoints)
    Xc, Zc = np.meshgrid(x, z)
    Yc = np.sqrt(self.radius ** 2 - Xc ** 2)
    ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=20, cstride=10)
    ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=20, cstride=10)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('{}'.format(self))
    return fig, ax