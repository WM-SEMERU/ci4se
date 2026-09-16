def get_instance(self, payload):
    return BindingInstance(self._version, payload, service_sid=self.
        _solution['service_sid'])