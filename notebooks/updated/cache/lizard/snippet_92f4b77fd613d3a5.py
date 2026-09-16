def _rewrite_source(self, s):
    new = [b('#!') + utf8(self.interpreter_fragment)]
    if self.is_python:
        new.append(self.b_ENCODING_STRING)
    _, _, rest = bytes_partition(s, b('\n'))
    new.append(rest)
    return b('\n').join(new)