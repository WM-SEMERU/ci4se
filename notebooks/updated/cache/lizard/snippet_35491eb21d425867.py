def build_lines_data(self, code_obj):
    if self.version > 1.4:
        linestarts = list(self.opc.findlinestarts(code_obj))
    else:
        linestarts = [[0, 1]]
    self.linestarts = dict(linestarts)
    lines = []
    LineTuple = namedtuple('LineTuple', ['l_no', 'next'])
    _, prev_line_no = linestarts[0]
    offset = 0
    for start_offset, line_no in linestarts[1:]:
        while offset < start_offset:
            lines.append(LineTuple(prev_line_no, start_offset))
            offset += 1
        prev_line_no = line_no
    codelen = len(self.code)
    while offset < codelen:
        lines.append(LineTuple(prev_line_no, codelen))
        offset += 1
    return lines