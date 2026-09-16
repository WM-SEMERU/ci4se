def get(self, *args, **kwargs):
    clone = self.filter(*args, **kwargs)
    if self.query.can_filter():
        clone = clone.order_by()
    num = len(clone)
    if num == 1:
        return clone._result_cache[0]
    if not num:
        raise self.resource.DoesNotExist(
            '%s matching query does not exist. Lookup parameters were %s' %
            (self.resource._meta.resource_name, kwargs))
    raise self.resource.MultipleObjectsReturned(
        'get() returned more than one %s -- it returned %s! Lookup parameters were %s'
         % (self.resource._meta.resource_name, num, kwargs))