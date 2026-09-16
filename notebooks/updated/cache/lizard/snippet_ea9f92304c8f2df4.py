def _read_frame(self):
    if self.skip_equi_period:
        while True:
            step, line = self.goto_next_frame()
            self._counter += 1
            if step >= self.equi_period:
                break
        self.skip_equi_period = False
    else:
        step, line = self.goto_next_frame()
    try:
        row = [step]
        for i in range(9):
            row.append(float(line[10 + i * 12:10 + (i + 1) * 12]))
        line = next(self._f)[:-1]
        row.append(float(line[:10]))
        for i in range(9):
            row.append(float(line[10 + i * 12:10 + (i + 1) * 12]))
        line = next(self._f)[:-1]
        row.append(float(line[:10]))
        for i in range(9):
            row.append(float(line[10 + i * 12:10 + (i + 1) * 12]))
    except ValueError:
        raise FileFormatError(
            'Some numbers in the output file could not be read. (expecting floating point numbers)'
            )
    for i in range(30):
        row[i] *= self._conv[i]
    return row