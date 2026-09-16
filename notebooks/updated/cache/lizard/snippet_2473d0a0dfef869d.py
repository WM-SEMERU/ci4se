def do_complete(self, code, cursor_pos):
    self._klog.info('{%s}', code[cursor_pos:cursor_pos + 10])
    token, start = token_at_cursor(code, cursor_pos)
    tkn_low = token.lower()
    if is_magic(token, start, code):
        matches = [k for k in magics.keys() if k.startswith(tkn_low)]
    else:
        matches = [sparql_names[k] for k in sparql_names if k.startswith(
            tkn_low)]
    self._klog.debug('token={%s} matches={%r}', token, matches)
    if matches:
        return {'status': 'ok', 'cursor_start': start, 'cursor_end': start +
            len(token), 'matches': matches}