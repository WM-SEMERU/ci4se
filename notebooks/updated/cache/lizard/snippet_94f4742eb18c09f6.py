def apply_new_scoped_variable_type(self, path, new_variable_type_str):
    data_port_id = self.list_store[path][self.ID_STORAGE_ID]
    try:
        if self.model.state.scoped_variables[data_port_id
            ].data_type.__name__ != new_variable_type_str:
            self.model.state.scoped_variables[data_port_id].change_data_type(
                new_variable_type_str)
    except ValueError as e:
        logger.error('Error while changing data type: {0}'.format(e))