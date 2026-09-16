def get_klass(self):
    klass_name = self.kwargs.get('klass', None)
    klass = self.registry.get(klass_name, None)
    if not klass:
        raise Http404('Unknown autocomplete class `{}`'.format(klass_name))
    return klass