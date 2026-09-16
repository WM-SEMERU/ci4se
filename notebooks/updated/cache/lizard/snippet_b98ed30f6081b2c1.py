def delete(self, manytomany=True, delete_fieldname=None, send_dispatch=True,
    onetoone=True, **kwargs):
    if get_dispatch_send() and self.__dispatch_enabled__:
        dispatch.call(self.__class__, 'pre_delete', instance=self, signal=
            self.tablename)
    if manytomany:
        for k, v in self._manytomany.items():
            getattr(self, k).clear()
    if onetoone:
        for k, v in self._onetoone.items():
            row = getattr(self, k)
            if row:
                row.delete()
    if delete_fieldname:
        if delete_fieldname is True:
            delete_fieldname = 'deleted'
        if not hasattr(self, delete_fieldname):
            raise KeyError('There is no %s property exists' % delete_fieldname)
        setattr(self, delete_fieldname, True)
        self.save()
    else:
        do_(self.table.delete(self.table.c[self._primary_field] == self.
            _key), self.get_session())
        self._key = None
        self._old_values = {}
    if send_dispatch and get_dispatch_send() and self.__dispatch_enabled__:
        dispatch.call(self.__class__, 'post_delete', instance=self, signal=
            self.tablename)