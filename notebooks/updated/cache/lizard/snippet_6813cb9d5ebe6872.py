def parse(self):
    if not self.parsed.get('migration'):
        raise ParseError("'migration' key is missing", YAML_EXAMPLE)
    self.check_dict_expected_keys({'options', 'versions'}, self.parsed[
        'migration'], 'migration')
    return self._parse_migrations()