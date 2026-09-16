def dom_id(self):
    parameter = 'DOMID'
    if parameter not in self._by:
        self._populate(by=parameter)
    return self._by[parameter]