def is_all_field_none(self):
    if self._id_ is not None:
        return False
    if self._created is not None:
        return False
    if self._updated is not None:
        return False
    if self._description is not None:
        return False
    if self._ip is not None:
        return False
    if self._status is not None:
        return False
    return True