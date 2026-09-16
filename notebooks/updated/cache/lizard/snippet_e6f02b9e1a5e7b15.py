def parse(self, text):
    self.text = text
    data = yaml_load(self.text)
    if data is None:
        raise exceptions.CatalogException('No YAML data in file')
    context = dict(root=self._dir)
    result = CatalogParser(data, context=context, getenv=self.getenv,
        getshell=self.getshell)
    if result.errors:
        raise exceptions.ValidationError(
            "Catalog '{}' has validation errors:\n\n{}".format(self.path,
            '\n'.join(result.errors)), result.errors)
    cfg = result.data
    self._entries = {}
    for entry in cfg['data_sources']:
        entry._catalog = self
        self._entries[entry.name] = entry
    self.metadata = cfg.get('metadata', {})
    self.name = self.name or cfg.get('name') or self.name_from_path
    self.description = self.description or cfg.get('description')