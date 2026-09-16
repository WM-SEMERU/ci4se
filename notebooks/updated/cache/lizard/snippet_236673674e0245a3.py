def format(self, record):
    if record.levelno == DEBUG:
        return self.debug_formatter.format(record)
    if record.levelno == INFO:
        return self.info_formatter.format(record)
    if record.levelno == ERROR:
        return self.error_formatter.format(record)
    if record.levelno == WARNING:
        return self.warning_formatter.format(record)
    if record.levelno == CRITICAL:
        return self.critical_formatter.format(record)