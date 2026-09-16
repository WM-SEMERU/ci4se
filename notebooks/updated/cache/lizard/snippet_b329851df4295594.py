def output_file(self):
    out_files = self.output_files
    if len(out_files) != 1:
        err_msg = 'output_file property is only valid if there is a single'
        err_msg += ' output file. Here there are '
        err_msg += '%d output files.' % len(out_files)
        raise ValueError(err_msg)
    return out_files[0]