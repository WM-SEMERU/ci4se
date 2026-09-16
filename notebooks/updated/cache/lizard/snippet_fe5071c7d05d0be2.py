async def callHandlers(self, record):
    c = self
    found = 0
    while c:
        for handler in c.handlers:
            found = found + 1
            if record.levelno >= handler.level:
                await handler.handle(record)
        if not c.propagate:
            c = None
        else:
            c = c.parent
    if found == 0:
        raise Exception('No handlers could be found for logger')