def _file_name(self, dtype_out_time, extension='nc'):
    if dtype_out_time is None:
        dtype_out_time = ''
    out_lbl = utils.io.data_out_label(self.intvl_out, dtype_out_time,
        dtype_vert=self.dtype_out_vert)
    in_lbl = utils.io.data_in_label(self.intvl_in, self.dtype_in_time, self
        .dtype_in_vert)
    start_year = utils.times.infer_year(self.start_date)
    end_year = utils.times.infer_year(self.end_date)
    yr_lbl = utils.io.yr_label((start_year, end_year))
    return '.'.join([self.name, out_lbl, in_lbl, self.model.name, self.run.
        name, yr_lbl, extension]).replace('..', '.')