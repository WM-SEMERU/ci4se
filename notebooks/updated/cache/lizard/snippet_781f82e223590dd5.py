def _add_cxnSp(self, connector_type, begin_x, begin_y, end_x, end_y):
    id_ = self._next_shape_id
    name = 'Connector %d' % (id_ - 1)
    flipH, flipV = begin_x > end_x, begin_y > end_y
    x, y = min(begin_x, end_x), min(begin_y, end_y)
    cx, cy = abs(end_x - begin_x), abs(end_y - begin_y)
    return self._element.add_cxnSp(id_, name, connector_type, x, y, cx, cy,
        flipH, flipV)