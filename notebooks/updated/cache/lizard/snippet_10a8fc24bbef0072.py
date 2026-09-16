def line_range(self):
    num_lines = len(self.text().split('\n'))
    end_line = self._start_line + num_lines - 1
    return self._start_line, end_line