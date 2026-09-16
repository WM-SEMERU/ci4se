def _check_data_port_id(self, data_port):
    for input_data_port_id, input_data_port in self.input_data_ports.items():
        if (data_port.data_port_id == input_data_port_id and data_port is not
            input_data_port):
            return False, 'data port id already existing in state'
    for output_data_port_id, output_data_port in self.output_data_ports.items(
        ):
        if (data_port.data_port_id == output_data_port_id and data_port is not
            output_data_port):
            return False, 'data port id already existing in state'
    return True, 'valid'