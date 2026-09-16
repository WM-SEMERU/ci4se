def _build_all_dependencies(self):
    ret = {}
    for model, schema in six.iteritems(self._models()):
        dep_list = self._build_dependent_model_list(schema)
        ret[model] = dep_list
    return ret