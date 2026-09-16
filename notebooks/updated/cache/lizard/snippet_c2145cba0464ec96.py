def decorate(self, record):
    attachments = {}
    if record.levelno >= logging.ERROR:
        attachments['color'] = 'warning'
    if record.levelno >= logging.CRITICAL:
        attachments['color'] = 'danger'
    attach_text = '{levelname}: {name} {module}.{funcName}:{lineno}'.format(
        levelname=record.levelname, name=record.name, module=record.module,
        funcName=record.funcName, lineno=record.lineno)
    attachments['text'] = attach_text
    attachments['fallback'] = attach_text
    return attachments