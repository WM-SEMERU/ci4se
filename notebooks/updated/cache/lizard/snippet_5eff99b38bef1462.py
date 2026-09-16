def complete_opt_format(self, text, *_):
    return [(t + ' ') for t in FORMATTERS if t.startswith(text)]