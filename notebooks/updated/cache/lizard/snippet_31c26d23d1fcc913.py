def _parse_table(self):
    reset = self._head
    self._head += 2
    try:
        self._push(contexts.TABLE_OPEN)
        padding = self._handle_table_style('\n')
    except BadRoute:
        self._head = reset
        self._emit_text('{')
        return
    style = self._pop()
    self._head += 1
    restore_point = self._stack_ident
    try:
        table = self._parse(contexts.TABLE_OPEN)
    except BadRoute:
        while self._stack_ident != restore_point:
            self._memoize_bad_route()
            self._pop()
        self._head = reset
        self._emit_text('{')
        return
    self._emit_table_tag('{|', 'table', style, padding, None, table, '|}')
    self._head -= 1