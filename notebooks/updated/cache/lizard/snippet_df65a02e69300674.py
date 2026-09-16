def _init_metadata(self, **kwargs):
    osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
    self._group_default = self._mdata['group']['default_boolean_values'][0]
    self._avatar_default = self._mdata['avatar']['default_id_values'][0]