def copy(self):
    o = self.__class__(self.target, self.block.copy(), self.style, self.
        is_visible, self.pos)
    o.slider_min = self.slider_min
    o.slider_max = self.slider_max
    return o