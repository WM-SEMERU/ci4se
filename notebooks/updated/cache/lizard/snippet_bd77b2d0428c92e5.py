def heatmap(self, partition=None, cmap=CM.Blues):
    if isinstance(self.dm, DistanceMatrix):
        length = self.dm.values.shape[0]
    else:
        length = self.dm.shape[0]
    datamax = float(np.abs(self.dm).max())
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ticks_at = [0, 0.5 * datamax, datamax]
    if partition:
        sorting = flatten_list(partition.get_membership())
        self.dm = self.dm.reorder(sorting)
    cax = ax.imshow(self.dm.values, interpolation='nearest', origin='lower',
        extent=[0.0, length, 0.0, length], vmin=0, vmax=datamax, cmap=cmap)
    cbar = fig.colorbar(cax, ticks=ticks_at, format='%1.2g')
    cbar.set_label('Distance')
    return fig