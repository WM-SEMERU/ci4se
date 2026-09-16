def connect(self, dests=[], name=None, id='', props={}):
    with self._mutex:
        if self.porttype == 'DataInPort' or self.porttype == 'DataOutPort':
            for prop in props:
                if prop in self.properties:
                    if props[prop] not in [x.strip() for x in self.
                        properties[prop].split(',')
                        ] and 'any' not in self.properties[prop].lower():
                        raise exceptions.IncompatibleDataPortConnectionPropsError
                for d in dests:
                    if prop in d.properties:
                        if props[prop] not in [x.strip() for x in d.
                            properties[prop].split(',')
                            ] and 'any' not in d.properties[prop].lower():
                            raise exceptions.IncompatibleDataPortConnectionPropsError
        if not name:
            name = self.name + '_'.join([d.name for d in dests])
        props = utils.dict_to_nvlist(props)
        profile = RTC.ConnectorProfile(name, id, [self._obj] + [d._obj for
            d in dests], props)
        return_code, profile = self._obj.connect(profile)
        if return_code != RTC.RTC_OK:
            raise exceptions.FailedToConnectError(return_code)
        self.reparse_connections()
        for d in dests:
            d.reparse_connections()