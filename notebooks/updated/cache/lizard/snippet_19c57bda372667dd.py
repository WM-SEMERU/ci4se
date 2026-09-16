def write(self, iterable):
    io_error_text = _('Error writing to file {filepath}.')
    io_error_text = io_error_text.format(filepath=self.path)
    try:
        with open(self.path, 'wb') as csvfile:
            csv_writer = csv.writer(csvfile, self.dialect)
            for line in iterable:
                csv_writer.writerow(list(encode_gen(line, encoding=self.
                    encoding)))
    except IOError:
        txt = _('Error opening file {filepath}.').format(filepath=self.path)
        try:
            post_command_event(self.main_window, self.StatusBarMsg, text=txt)
        except TypeError:
            pass
        return False