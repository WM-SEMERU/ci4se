def value(self):
    field_vals = None
    field_names = self.fields_select.names()
    fcount = len(field_names)
    if fcount:
        d = self._query('get_one')
        if d:
            field_vals = [d.get(fn, None) for fn in field_names]
            if fcount == 1:
                field_vals = field_vals[0]
    else:
        raise ValueError('no select fields were set, so cannot return value')
    return field_vals