def knit(self, input_file, opts_chunk='eval=FALSE'):
    tmp_in = tempfile.NamedTemporaryFile(mode='w+')
    tmp_out = tempfile.NamedTemporaryFile(mode='w+')
    tmp_in.file.write(input_file.read())
    tmp_in.file.flush()
    tmp_in.file.seek(0)
    self._knit(tmp_in.name, tmp_out.name, opts_chunk)
    tmp_out.file.flush()
    return tmp_out