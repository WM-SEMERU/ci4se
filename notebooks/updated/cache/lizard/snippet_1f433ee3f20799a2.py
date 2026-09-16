def is_code(self):
    if self.cell_type == 'code':
        return True
    if self.cell_type == 'raw' and 'active' in self.metadata:
        return True
    return False