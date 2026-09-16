def update_terms(self, project_id, data, fuzzy_trigger=None):
    kwargs = {}
    if fuzzy_trigger is not None:
        kwargs['fuzzy_trigger'] = fuzzy_trigger
    data = self._run(url_path='terms/update', id=project_id, data=json.
        dumps(data), **kwargs)
    return data['result']['terms']