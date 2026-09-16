def options(self):
    config = self._config
    o = {}
    o.update(self._default_smtp_options)
    o.update(self._default_message_options)
    o.update(self._default_backend_options)
    o.update(get_namespace(config, 'EMAIL_', valid_keys=o.keys()))
    o['port'] = int(o['port'])
    o['timeout'] = float(o['timeout'])
    return o