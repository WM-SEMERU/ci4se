def _get_xlsx_kws(self, **kws_usr):
    kws_xlsx = {'fld2col_widths': self._get_fld2col_widths(**kws_usr),
        'items': 'GO IDs'}
    remaining_keys = set(['title', 'hdrs', 'prt_flds', 'fld2fmt',
        'ntval2wbfmtdict', 'ntfld_wbfmt'])
    for usr_key, usr_val in kws_usr.items():
        if usr_key in remaining_keys:
            kws_xlsx[usr_key] = usr_val
    return kws_xlsx