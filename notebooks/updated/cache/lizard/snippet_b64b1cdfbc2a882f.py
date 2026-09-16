def find_attr_start_line(self, lines, min_line=4, max_line=9):
    for idx, line in enumerate(lines[min_line:max_line]):
        col = line.split()
        if len(col) > 1 and col[1] == 'ATTRIBUTE_NAME':
            return idx + min_line + 1
    self.log.warn(
        'ATTRIBUTE_NAME not found in second column of smartctl output between lines %d and %d.'
         % (min_line, max_line))
    return max_line + 1