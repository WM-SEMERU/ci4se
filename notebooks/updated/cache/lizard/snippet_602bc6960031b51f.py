def update_instance(self, data):
    for key, val in iteritems(data):
        if not hasattr(self, key):
            raise AttributeError('No field named {key} for model {model}'.
                format(key=key, model=self.__class__.__name__))
        setattr(self, key, val)
    self.save()
    return self