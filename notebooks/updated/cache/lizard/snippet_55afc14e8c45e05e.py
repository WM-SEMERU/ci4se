def _config_to_text(self):
    r = ''
    for k in self._config:
        cosa = '\n        '.join(self._config[k]) + '\n'
        r += k + ': ' + cosa
    r += '\n'
    return r