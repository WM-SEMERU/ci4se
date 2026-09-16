def draw(self):
    sizes = self._get_cluster_sizes()
    self.ax.scatter(self.embedded_centers_[:, (0)], self.embedded_centers_[
        :, (1)], s=sizes, c=self.facecolor, edgecolor=self.edgecolor,
        linewidth=1)
    for i, pt in enumerate(self.embedded_centers_):
        self.ax.text(s=str(i), x=pt[0], y=pt[1], va='center', ha='center',
            fontweight='bold')
    plt.sca(self.ax)
    return self.ax