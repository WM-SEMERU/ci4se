def _select_graphic_rendition(self, *attrs):
    if len(attrs) == 0:
        attrs = [0]
    for attr in attrs:
        self._set_attr(attr)