def _with_rotation(self, w, h):
    res_w = abs(w * math.cos(self.rotation) + h * math.sin(self.rotation))
    res_h = abs(h * math.cos(self.rotation) + w * math.sin(self.rotation))
    return res_w, res_h