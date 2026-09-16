def get_templates_per_page(self, per_page=1000, page=1, params=None):
    return self._get_resource_per_page(resource=TEMPLATES, per_page=
        per_page, page=page, params=params)