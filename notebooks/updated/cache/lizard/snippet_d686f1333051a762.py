def get_referenced_object(self):
    if self._UserPerson is not None:
        return self._UserPerson
    if self._UserCompany is not None:
        return self._UserCompany
    raise exception.BunqException(self._ERROR_NULL_FIELDS)