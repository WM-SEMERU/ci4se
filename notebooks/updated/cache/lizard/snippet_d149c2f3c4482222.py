def hide(self):
    self._hidden = True
    for artist in self.annotations.values():
        artist.set_visible(False)
    for fig in self.figures:
        fig.canvas.draw()
    return self