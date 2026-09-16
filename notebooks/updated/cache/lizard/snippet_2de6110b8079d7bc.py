def apply_operation_to(self, path):
    return path.add_lnTo(self._x - self._freeform_builder.shape_offset_x, 
        self._y - self._freeform_builder.shape_offset_y)