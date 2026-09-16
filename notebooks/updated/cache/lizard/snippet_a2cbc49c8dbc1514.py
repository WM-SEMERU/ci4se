def resetLoggingLocks():
    try:
        logging._releaseLock()
    except RuntimeError:
        pass
    for handler in logging.Logger.manager.loggerDict.values():
        if hasattr(handler, 'lock') and handler.lock:
            try:
                handler.lock.release()
            except RuntimeError:
                pass