def load_object(self, kwargs):
    self.object = None
    self.config = None
    self.model = self.get_model_class()
    kwargs.pop('app', None)
    kwargs.pop('model', None)
    if self.model and kwargs.get('pk', False):
        try:
            self.object = self.model.objects.get(pk=kwargs.pop('pk'))
        except Exception:
            raise Exception('Could not load {}'.format(self.model.__name__.
                lower()))
        setattr(self, self.model.__name__.lower(), self.object)
    return kwargs