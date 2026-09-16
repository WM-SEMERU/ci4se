def is_all_field_none(self):
    if self._attachment_public_uuid is not None:
        return False
    if self._content_type is not None:
        return False
    if self._height is not None:
        return False
    if self._width is not None:
        return False
    return True