def _resolve_capability(self, atom):
    code = tigetstr(self._sugar.get(atom, atom))
    if code:
        return code.decode('latin1')
    return ''