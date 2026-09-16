def is_all_field_none(self):
    if self._avatar is not None:
        return False
    if self._title is not None:
        return False
    if self._sub_title is not None:
        return False
    return True