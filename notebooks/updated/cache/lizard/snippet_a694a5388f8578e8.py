def handle_symbol_search(self, call_id, payload):
    self.log.debug('handle_symbol_search: in %s', Pretty(payload))
    syms = payload['syms']
    qfList = []
    for sym in syms:
        p = sym.get('pos')
        if p:
            item = self.editor.to_quickfix_item(str(p['file']), p['line'],
                str(sym['name']), 'info')
            qfList.append(item)
    self.editor.write_quickfix_list(qfList, 'Symbol Search')