def _handle_error(self, text, ErrorClass, infile, cur_index):
    line = infile[cur_index]
    cur_index += 1
    message = text % cur_index
    error = ErrorClass(message, cur_index, line)
    if self.raise_errors:
        raise error
    self._errors.append(error)