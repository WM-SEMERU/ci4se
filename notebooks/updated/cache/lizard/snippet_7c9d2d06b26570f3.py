def _normalize_select(self, query):
    if 'select' not in query:
        return
    if isinstance(query['select'], string_class()):
        query['select'] = [s.strip() for s in query['select'].split(',')]
    query['select'] = [s for s in query['select'] if not s.startswith('sys.')]
    if 'sys' not in query['select']:
        query['select'].append('sys')