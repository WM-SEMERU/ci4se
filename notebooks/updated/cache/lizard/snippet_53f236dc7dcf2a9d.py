def make_scope(self, col_scope_list=None, row_scope_list=None):
    if col_scope_list is not None and len(col_scope_list) > 0:
        self.apply_scope(col_scope_list, 'col')
    if row_scope_list is not None and len(row_scope_list) > 0:
        self.apply_scope(row_scope_list, 'row')