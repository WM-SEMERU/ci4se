def get_options_for_model(self, model):
    opts = self._get_options_for_model(model)
    if not opts.registered and not opts.related:
        raise NotRegistered(
            'The model "%s" is not registered for translation' % model.__name__
            )
    return opts