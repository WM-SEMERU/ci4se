def get_end_offset(self, value, parent=None, index=None):
    return self.get_start_offset(value, parent, index) + self.get_size(value,
        parent, index)