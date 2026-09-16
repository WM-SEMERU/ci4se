def do_glob_math(self, cont):
    if not isinstance(cont, six.string_types):
        warn(FutureWarning(
            'do_glob_math was passed a non-string {0!r} -- this will no longer be supported in pyScss 2.0'
            .format(cont)))
        cont = six.text_type(cont)
    if '#{' not in cont:
        return cont
    cont = _expr_glob_re.sub(self._pound_substitute, cont)
    return cont