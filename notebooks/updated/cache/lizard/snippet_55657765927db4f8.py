def get_instance(self, payload):
    return IpAccessControlListInstance(self._version, payload, trunk_sid=
        self._solution['trunk_sid'])