def read(self, entity=None, attrs=None, ignore=None, params=None):
    if entity is None:
        entity = TemplateInput(self._server_config, template=self.template)
    if ignore is None:
        ignore = set()
    ignore.add('advanced')
    return super(TemplateInput, self).read(entity=entity, attrs=attrs,
        ignore=ignore, params=params)