def get_queryset(self, **kwargs):
    queryset = self.derive_queryset(**kwargs)
    return self.order_queryset(queryset)