def log_stack(logger, level=logging.INFO, limit=None, frame=None):
    if showing_stack.inside:
        return
    showing_stack.inside = True
    try:
        if frame is None:
            frame = sys._getframe(1)
        stack = ''.join(traceback.format_stack(frame, limit))
        for line in (l[2:] for l in stack.split('\n') if l.strip()):
            logger.log(level, line)
    finally:
        showing_stack.inside = False