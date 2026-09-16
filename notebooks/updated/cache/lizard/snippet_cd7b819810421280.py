def num_elements(self):
    if self.is_fully_defined():
        size = 1
        for dim in self._dims:
            size *= dim.value
        return size
    else:
        return None