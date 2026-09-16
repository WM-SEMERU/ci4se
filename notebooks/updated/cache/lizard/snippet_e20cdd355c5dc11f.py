def apply_filter_rule(self, _filter, query='in:inbox', way='in'):
    if isinstance(_filter, zobjects.FilterRule):
        _filter = _filter.name
    content = {'filterRules': {'filterRule': {'name': _filter}}, 'query': {
        '_content': query}}
    if way == 'in':
        ids = self.request('ApplyFilterRules', content)
    elif way == 'out':
        ids = self.request('ApplyOutgoingFilterRules', content)
    if ids:
        return [int(m) for m in ids['m']['ids'].split(',')]
    else:
        return []