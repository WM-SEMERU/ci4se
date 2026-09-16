def write_output_data(self, specific_output_dictionary=None):
    if isinstance(specific_output_dictionary, dict):
        output_dict = specific_output_dictionary
    else:
        output_dict = self.output_data
    for output_name, value in self.output_data.items():
        output_port_id = self.get_io_data_port_id_from_name_and_type(
            output_name, OutputDataPort)
        actual_value = None
        actual_value_was_written = False
        actual_value_time = 0
        for data_flow_id, data_flow in self.data_flows.items():
            if data_flow.to_state == self.state_id:
                if data_flow.to_key == output_port_id:
                    scoped_data_key = str(data_flow.from_key
                        ) + data_flow.from_state
                    if scoped_data_key in self.scoped_data:
                        if actual_value is None or self.scoped_data[
                            scoped_data_key].timestamp > actual_value_time:
                            actual_value = deepcopy(self.scoped_data[
                                scoped_data_key].value)
                            actual_value_time = self.scoped_data[
                                scoped_data_key].timestamp
                            actual_value_was_written = True
                    elif not self.backward_execution:
                        logger.debug(
                            'Output data with name {0} of state {1} was not found in the scoped data of state {2}. Thus the state did not write onto this output. This can mean a state machine design error.'
                            .format(str(output_name), str(self.states[
                            data_flow.from_state].get_path()), self.get_path())
                            )
        if actual_value_was_written:
            output_dict[output_name] = actual_value