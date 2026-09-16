def append_id(self, id_col_name='append_id', cols=None):
    from .. import preprocess
    if id_col_name in self.schema:
        raise ValueError('ID column collides with existing columns.')
    append_id_obj = getattr(preprocess, '_AppendID')(id_col=id_col_name,
        selected_cols=cols)
    return append_id_obj.transform(self)