def _custom_icon(self, name, **kwargs):
    options = dict(_default_options, **kwargs)
    if name in self.painters:
        painter = self.painters[name]
        return self._icon_by_painter(painter, options)
    else:
        return QIcon()