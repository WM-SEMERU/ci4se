def format(self, filename, line, timestamp, **kwargs):
    line = unicode(line.encode('utf-8'), 'utf-8', errors='ignore')
    formatter = self._beaver_config.get_field('format', filename)
    if formatter not in self._formatters:
        formatter = self._default_formatter
    data = {self._fields.get('type'): kwargs.get('type'), self._fields.get(
        'tags'): kwargs.get('tags'), '@timestamp': timestamp, self._fields.
        get('host'): self._current_host, self._fields.get('file'): filename,
        self._fields.get('message'): line}
    if self._logstash_version == 0:
        data['@source'] = 'file://{0}'.format(filename)
        data['@fields'] = kwargs.get('fields')
    else:
        data['@version'] = self._logstash_version
        fields = kwargs.get('fields')
        for key in fields:
            data[key] = fields.get(key)
    return self._formatters[formatter](data)