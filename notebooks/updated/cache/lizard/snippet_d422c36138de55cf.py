def parse_verilog_file(fname):
    with open(fname, 'rt') as fh:
        text = fh.read()
    return parse_verilog(text)