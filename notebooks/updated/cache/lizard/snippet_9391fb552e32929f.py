def simulate(self, text, using='default', explain=False, attributes=None):
    es = connections.get_connection(using)
    body = {'text': text, 'explain': explain}
    if attributes:
        body['attributes'] = attributes
    definition = self.get_analysis_definition()
    analyzer_def = self.get_definition()
    for section in ('tokenizer', 'char_filter', 'filter'):
        if section not in analyzer_def:
            continue
        sec_def = definition.get(section, {})
        sec_names = analyzer_def[section]
        if isinstance(sec_names, six.string_types):
            body[section] = sec_def.get(sec_names, sec_names)
        else:
            body[section] = [sec_def.get(sec_name, sec_name) for sec_name in
                sec_names]
    if self._builtin_type != 'custom':
        body['analyzer'] = self._builtin_type
    return AttrDict(es.indices.analyze(body=body))