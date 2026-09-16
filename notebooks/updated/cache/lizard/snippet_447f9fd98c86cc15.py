def _emit_error(cls, message):
    sys.stderr.write('ERROR: {message}\n'.format(message=message))
    sys.stderr.flush()