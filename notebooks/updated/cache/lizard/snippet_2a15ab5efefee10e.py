def copy(self):
    templates = self.prepare_templates()
    if self.params.interactive:
        keys = list(self.parser.default)
        for key in keys:
            if key.startswith('_'):
                continue
            prompt = '{0} (default is "{1}")? '.format(key, self.parser.
                default[key])
            if _compat.PY2:
                value = raw_input(prompt.encode('utf-8')).decode('utf-8')
            else:
                value = input(prompt.encode('utf-8'))
            value = value.strip()
            if value:
                self.parser.default[key] = value
    self.parser.default['templates'] = tt = ','.join(t.name for t in templates)
    logging.warning('Paste templates: {0}'.format(tt))
    self.make_directory(self.params.TARGET)
    logging.debug('\nDefault context:\n----------------')
    logging.debug(''.join('{0:<15} {1}\n'.format(*v) for v in self.parser.
        default.items()))
    return [t.paste(**dict(self.parser.default.items())) for t in templates]