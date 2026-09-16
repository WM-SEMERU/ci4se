def line_join_type(self):
    key = self._data.get(b'strokeStyleLineJoinType').enum
    return self.STROKE_STYLE_LINE_JOIN_TYPES.get(key, str(key))