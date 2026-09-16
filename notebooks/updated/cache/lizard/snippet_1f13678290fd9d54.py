def _clean_dirty_objects(self):
    if self._dirty_object is None:
        return
    if not is_iterable_but_not_string(self._dirty_object):
        self._dirty_object = [self._dirty_object]
    log.debug('Cleaning objects: {}'.format(self._dirty_object))
    for o in self._dirty_object:
        if isinstance(o, BaseObject):
            o._clean_dirty()
    self._dirty_object = None