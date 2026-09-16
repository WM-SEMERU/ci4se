def _get_next_n(self, object_class, number=None):
    if number > self.available():
        raise errors.IllegalState('not enough elements available in this list')
    else:
        next_list = []
        counter = 0
        while counter < number:
            try:
                next_list.append(next(self))
            except Exception:
                raise errors.OperationFailed()
            counter += 1
        return object_class(next_list)