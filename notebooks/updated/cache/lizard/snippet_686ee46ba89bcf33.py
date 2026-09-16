def get_model_name(self):
    if self.model_name is None:
        raise ImproperlyConfigured(
            "%s requires either a definition of 'model_name' or an implementation of 'get_model_name()'"
             % self.__class__.__name__)
    return self.model_name