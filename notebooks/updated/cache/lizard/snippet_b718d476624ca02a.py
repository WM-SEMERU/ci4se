def is_all_field_none(self):
    if self._id_ is not None:
        return False
    if self._created is not None:
        return False
    if self._updated is not None:
        return False
    if self._year is not None:
        return False
    if self._alias_user is not None:
        return False
    return True