def incident(self, name, **kwargs):
    group_obj = Incident(name, **kwargs)
    return self._group(group_obj)