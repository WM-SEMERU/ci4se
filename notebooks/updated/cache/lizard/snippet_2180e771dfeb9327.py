def get(self, using=None, **kwargs):
    return self._get_connection(using).indices.get(index=self._name, **kwargs)