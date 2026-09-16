def _add_model(self, model):
    name = model._name
    existing = self._models.get(name, None)
    if not existing:
        self._models[name] = model
    elif model.__name__ != existing.__name__ or model._creation_source != existing._creation_source:
        raise ImplementationError(
            'A model with namespace "%s" and name "%s" is already defined on this database'
             % (model.namespace, model.__name__))
    return self._models[name]