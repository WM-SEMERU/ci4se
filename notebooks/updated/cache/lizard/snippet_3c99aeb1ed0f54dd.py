def delete(self):
    check_bind(self)
    if self.id is None:
        raise ServerError('{} object does not exist yet'.format(self.
            __class__.name))
    elif not self.__class__._has_schema_method('destroy'):
        raise MethodNotSupported('{} do not support deletion.'.format(self.
            __class__.__name__))
    try:
        self._resource.delete()
    except HTTPError as e:
        if e.response.status_code == 403:
            raise PermissionDenied('')
        else:
            raise e