def get_type(self):
    if self.type_idx_value == None:
        self.type_idx_value = self.CM.get_type(self.type_idx)
    return self.type_idx_value