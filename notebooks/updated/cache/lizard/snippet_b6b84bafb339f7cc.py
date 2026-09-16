def convert_level(self, record):
    level = record.levelno
    if level >= logging.CRITICAL:
        return levels.CRITICAL
    if level >= logging.ERROR:
        return levels.ERROR
    if level >= logging.WARNING:
        return levels.WARNING
    if level >= logging.INFO:
        return levels.INFO
    return levels.DEBUG