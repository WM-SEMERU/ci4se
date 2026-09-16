def write(self, fname=None, filtered=False, header=True, append=False):
    r
    write_ex = pexdoc.exh.addex(ValueError, 'There is no data to save to file')
    fname = self._fname if fname is None else fname
    data = self.data(filtered=filtered)
    write_ex(len(data) == 0 or len(data) == 1 and len(data[0]) == 0)
    if header:
        header = [header] if isinstance(header, str) else header
        cfilter = self._gen_col_index(filtered=filtered)
        filtered_header = [self._header[item] for item in cfilter
            ] if self._has_header else cfilter
        file_header = filtered_header if isinstance(header, bool) else header
    data = [[("''" if item is None else item) for item in row] for row in data]
    _write_int(fname, [file_header] + data if header else data, append=append)