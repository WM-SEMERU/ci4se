def set_default(self, field):
    if field in RECORD_SPECS.index:
        if RECORD_SPECS.loc[field, 'write_default'] is None or getattr(self,
            field) is not None:
            return
        setattr(self, field, RECORD_SPECS.loc[field, 'write_default'])
    elif field in SIGNAL_SPECS.index:
        if field == 'file_name' and self.file_name is None:
            self.file_name = self.n_sig * [self.record_name + '.dat']
            return
        item = getattr(self, field)
        if SIGNAL_SPECS.loc[field, 'write_default'
            ] is None or item is not None:
            return
        if field == 'adc_res' and self.fmt is not None:
            self.adc_res = _signal._fmt_res(self.fmt)
            return
        setattr(self, field, [SIGNAL_SPECS.loc[field, 'write_default']] *
            self.n_sig)