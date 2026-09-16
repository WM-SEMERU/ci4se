def get_io_data_port_id_from_name_and_type(self, name, data_port_type):
    if data_port_type is InputDataPort:
        for ip_id, output_port in self.input_data_ports.items():
            if output_port.name == name:
                return ip_id
        raise AttributeError("Name '{0}' is not in input_data_ports".format
            (name))
    elif data_port_type is OutputDataPort:
        for op_id, output_port in self.output_data_ports.items():
            if output_port.name == name:
                return op_id
        if name == 'error':
            return
        raise AttributeError("Name '{0}' is not in output_data_ports".
            format(name))