def get_email_templates(self, params=None):
    if not params:
        params = {}
    return self._iterate_through_pages(self.get_email_templates_per_page,
        resource=EMAIL_TEMPLATES, **{'params': params})