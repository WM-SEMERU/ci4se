def scale(self, vmin=0.0, vmax=1.0):
    return StepColormap(self.colors, index=[(vmin + (vmax - vmin) * (x -
        self.vmin) * 1.0 / (self.vmax - self.vmin)) for x in self.index],
        vmin=vmin, vmax=vmax)