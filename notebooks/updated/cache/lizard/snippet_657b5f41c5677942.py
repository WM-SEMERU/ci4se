def template_id(self, value):
    if isinstance(value, TemplateId):
        self._template_id = value
    else:
        self._template_id = TemplateId(value)