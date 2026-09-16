def _set_boolean_property(self, propname, value):
    if value not in (True, False):
        raise ValueError(
            'assigned value must be either True or False, got %s' % value)
    tblPr = self.get_or_add_tblPr()
    setattr(tblPr, propname, value)