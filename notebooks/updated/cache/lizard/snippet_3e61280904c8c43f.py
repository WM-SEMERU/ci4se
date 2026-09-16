def port_uris_prop(self):
    if self._port_uris_prop is None:
        family = self.get_property('adapter-family')
        try:
            self._port_uris_prop = self.port_uris_prop_by_family[family]
        except KeyError:
            self._port_uris_prop = ''
    return self._port_uris_prop