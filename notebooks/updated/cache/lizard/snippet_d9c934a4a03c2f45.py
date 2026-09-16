def get_resources(self, request, **resources):
    if self.parent:
        resources = self.parent.get_resources(request, **resources)
    pks = resources.get(self._meta.name) or request.REQUEST.getlist(self.
        _meta.name) or getattr(request, 'data', None) and request.data.get(self
        ._meta.name)
    if not pks or self._meta.queryset is None:
        return resources
    pks = as_tuple(pks)
    try:
        if len(pks) == 1:
            resources[self._meta.name] = self._meta.queryset.get(pk=pks[0])
        else:
            resources[self._meta.name] = self._meta.queryset.filter(pk__in=pks)
    except (ObjectDoesNotExist, ValueError, AssertionError):
        raise HttpError('Resource not found.', status=status.HTTP_404_NOT_FOUND
            )
    except MultipleObjectsReturned:
        raise HttpError('Resources conflict.', status=status.HTTP_409_CONFLICT)
    return resources