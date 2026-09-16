def shape_offset_x(self):
    min_x = self._start_x
    for drawing_operation in self:
        if hasattr(drawing_operation, 'x'):
            min_x = min(min_x, drawing_operation.x)
    return min_x