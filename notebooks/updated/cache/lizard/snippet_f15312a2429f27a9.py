def start_traffic(self, blocking=False, *ports):
    for chassis, chassis_ports in self._per_chassis_ports(*self.
        _get_operation_ports(*ports)).items():
        chassis.start_traffic(False, *chassis_ports)
    if blocking:
        for chassis, chassis_ports in self._per_chassis_ports(*self.
            _get_operation_ports(*ports)).items():
            chassis.wait_traffic(*chassis_ports)