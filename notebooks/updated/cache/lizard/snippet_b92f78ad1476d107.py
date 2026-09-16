def find_all(self, model_class, params={}):
    url = '{host}/{namespace}/{model}{params}'.format(host=self._host,
        namespace=self._namespace, model=self._translate_name(model_class.
        __name__), params=self._build_param_string(params))
    data = self._get_json(url)['data']
    fresh_models = []
    for item in data:
        fresh_model = model_class(item['attributes'])
        fresh_model.id = item['id']
        fresh_model.validate()
        fresh_models.append(fresh_model)
        if self._cache is not None:
            self._cache.set_record(model_class.__name__, fresh_model.id,
                fresh_model)
    return fresh_models