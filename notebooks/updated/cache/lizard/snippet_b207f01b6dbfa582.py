def log(self, message, severity=INFO, tag=''):
    entry = _LogEntry(severity=severity, time=datetime.datetime.now(), tag=
        tag, indentation=self.indentation, message=self._sanitize(message))
    self.entries.append(entry)
    if self.tee:
        gf.safe_print(entry.pretty_print(show_datetime=self.tee_show_datetime))
    return entry.time