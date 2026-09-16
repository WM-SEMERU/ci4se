def getbug(self, objid, include_fields=None, exclude_fields=None,
    extra_fields=None):
    data = self._getbug(objid, include_fields=include_fields,
        exclude_fields=exclude_fields, extra_fields=extra_fields)
    return Bug(self, dict=data, autorefresh=self.bug_autorefresh)