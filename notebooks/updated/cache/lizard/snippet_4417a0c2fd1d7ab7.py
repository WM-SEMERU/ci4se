def tickets(self, extra_params=None):
    params = {'per_page': settings.MAX_PER_PAGE, 'report': 0}
    if extra_params:
        params.update(extra_params)
    return self.api._get_json(Ticket, space=self, rel_path=self.
        _build_rel_path('tickets'), extra_params=params, get_all=True)