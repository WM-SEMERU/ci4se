def add_input_data_port(self, name, data_type=None, default_value=None,
    data_port_id=None):
    if data_port_id is None:
        data_port_id = generate_data_port_id(self.get_data_port_ids())
    self._input_data_ports[data_port_id] = InputDataPort(name, data_type,
        default_value, data_port_id, self)
    valid, message = self._check_data_port_name(self._input_data_ports[
        data_port_id])
    if not valid:
        self._input_data_ports[data_port_id].parent = None
        del self._input_data_ports[data_port_id]
        raise ValueError(message)
    return data_port_id