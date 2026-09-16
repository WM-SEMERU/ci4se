def on_resize(self, event):
    if self._aspect is None:
        return
    w, h = self._canvas.size
    aspect = self._aspect / (w / h)
    self.scale = self.scale[0], self.scale[0] / aspect
    self.shader_map()