def get_lines(fname):
    for line in fileinput.input(fname):
        yield fileinput.filelineno(), line.strip()