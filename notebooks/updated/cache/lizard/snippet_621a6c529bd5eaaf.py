def configure_data(self, data, key_string=''):
    if len(data.keys()) == 0:
        return
    key_parts = key_string.rsplit('.')
    prefix = '  ' * (len(key_parts) - 1)
    label = self.data.get_label(key_string)
    if label:
        p = prefix
        if len(p) > 0:
            p += ' '
        self.prompt.header(p + '[' + label + ']')
    prefix = prefix + '   '
    if '_enabled' in data.keys():
        s = self.data.get_key_string(key_string, '_enabled')
        data['_enabled'] = self.prompt.bool(prefix + self.data.get_label(s),
            None, data['_enabled'])
        if data['_enabled'] is False:
            return
    for k, v in data.iteritems():
        if k == '_enabled':
            continue
        t = type(v)
        s = self.data.get_key_string(key_string, k)
        if t is dict:
            self.configure_data(v, s)
        else:
            label = prefix + self.data.get_label(s)
            self.parse_value(data, label, s, None, v)