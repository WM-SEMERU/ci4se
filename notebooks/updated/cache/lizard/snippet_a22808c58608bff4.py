def segments(self, using=None, **kwargs):
    return self._get_connection(using).indices.segments(index=self._name,
        **kwargs)