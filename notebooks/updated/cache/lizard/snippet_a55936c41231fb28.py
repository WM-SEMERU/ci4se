def set_viewbox(self, x, y, w, h):
    self.attributes['viewBox'] = '%s %s %s %s' % (x, y, w, h)
    self.attributes['preserveAspectRatio'] = 'none'