def collect_aliases(self):
    self.aliases = get_aliases(self._code_lines)
    for alias, signature in self.aliases.items():
        _, _, requires = parse_signature(signature)
        self.required_types |= requires
        self.defined_types |= {alias}