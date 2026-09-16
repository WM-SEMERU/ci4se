def _to_unicode(instr):
    if instr is None or isinstance(instr, six.text_type):
        return instr
    else:
        return six.text_type(instr, 'utf8')