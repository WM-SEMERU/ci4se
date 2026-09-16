def _init_metadata(self, **kwargs):
    osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
    self._grade_system_default = self._mdata['grade_system'][
        'default_id_values'][0]