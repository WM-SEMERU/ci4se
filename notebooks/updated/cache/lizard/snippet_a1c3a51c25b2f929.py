def _control_line(self, line):
    if line > float(self.LINE_LAST_PIXEL):
        return int(self.LINE_LAST_PIXEL)
    elif line < float(self.LINE_FIRST_PIXEL):
        return int(self.LINE_FIRST_PIXEL)
    else:
        return line