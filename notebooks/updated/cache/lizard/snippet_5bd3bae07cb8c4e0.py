def print_info(*messages, **kwargs):
    sep = kwargs.pop('sep', ' ')
    frame = sys._getframe(1)
    ln = frame.f_lineno
    _file = frame.f_globals.get('__file__', '')
    fn = os.path.split(_file)[-1]
    return print_logger.info(sep.join(map(unicode, messages)), extra={'ln':
        ln, 'fn': fn})