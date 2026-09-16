def _resolve_match_data(self, ref, event_data):
    if self.caller is None:
        pass
    elif ref is not self.caller:
        return False
    try:
        dat = event_data if IS_PYTHON3 else event_data.decode('utf-8')
        if self.match_data.startswith('regex:'):
            splt = self.match_data.split(':', 1)
            pttrn = re.compile(splt[1])
            match = re.search(pttrn, dat)
            return match if match is not None else False
        return event_data if self.match_data in dat else False
    except UnicodeDecodeError:
        dat = repr(event_data)
        return self._resolve_match_data(ref, dat)