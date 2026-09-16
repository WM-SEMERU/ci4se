def parse_flask_section(self):
    if self.has_section('flask'):
        for item in self.items('flask'):
            self._load_item(item[0])
    else:
        warnings.warn('No [flask] section found in config')