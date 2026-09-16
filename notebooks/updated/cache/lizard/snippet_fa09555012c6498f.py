def plot(self, save_path=None, close=False, bbox_inches='tight', pad_inches=1):
    for plot in self.subplots.flatten():
        plot.set_xlim(-0.1, 1.1)
        plot.set_ylim(-0.1, 1.1)
        plot.axis('off')
    if save_path:
        plt.savefig(save_path, transparent=True, dpi=300, bbox_inches=
            bbox_inches, pad_inches=pad_inches)
    if close:
        plt.close()