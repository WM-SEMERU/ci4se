def get_snmp_service(self):
    return SnmpContextManager(self.enable_flow, self.disable_flow, self.
        _snmp_parameters, self._logger)