def put_alias(self, using=None, **kwargs):
    return self._get_connection(using).indices.put_alias(index=self._name,
        **kwargs)