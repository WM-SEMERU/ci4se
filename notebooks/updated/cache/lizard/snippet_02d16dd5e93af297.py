def format(self, record):
    self._format_record(record)
    record_dict = {}
    for k, v in record.__dict__.items():
        if isinstance(k, str):
            k = decode_(k, 'utf8')
        if isinstance(v, str):
            v = decode_(v, 'utf8', 'replace')
        record_dict[k] = v
    if 'color' in self.fmt or 'end_color' in self.fmt:
        record_dict['color'], record_dict['end_color'] = _color(record.levelno)
    log = self.ufmt % record_dict
    if record.exc_text:
        if log[-1:] != '\n':
            log += '\n'
        log += decode_(record.exc_text, 'utf8', 'replace')
    log = log.replace('\n', '\n' + self.tab)
    return log