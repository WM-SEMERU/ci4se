def update(self, request, *args, **kwargs):
    with transaction.atomic():
        return self._update(request, *args, **kwargs)