def filter_input_variables(self, input_data_frame=None, simulation=None):
    assert input_data_frame is not None
    assert simulation is not None
    id_variable_by_entity_key = self.id_variable_by_entity_key
    role_variable_by_entity_key = self.role_variable_by_entity_key
    used_as_input_variables = self.used_as_input_variables
    tax_benefit_system = simulation.tax_benefit_system
    variables = tax_benefit_system.variables
    id_variables = [id_variable_by_entity_key[_entity.key] for _entity in
        simulation.entities.values() if not _entity.is_person]
    role_variables = [role_variable_by_entity_key[_entity.key] for _entity in
        simulation.entities.values() if not _entity.is_person]
    log.debug('Variable used_as_input_variables in filter: \n {}'.format(
        used_as_input_variables))
    unknown_columns = []
    for column_name in input_data_frame:
        if column_name in id_variables + role_variables:
            continue
        if column_name not in variables:
            unknown_columns.append(column_name)
            input_data_frame.drop(column_name, axis=1, inplace=True)
    if unknown_columns:
        log.debug(
            'The following unknown columns {}, are dropped from input table'
            .format(sorted(unknown_columns)))
    used_columns = []
    dropped_columns = []
    for column_name in input_data_frame:
        if column_name in id_variables + role_variables:
            continue
        variable = variables[column_name]
        if variable.formulas:
            if column_name in used_as_input_variables:
                used_columns.append(column_name)
                continue
            dropped_columns.append(column_name)
            input_data_frame.drop(column_name, axis=1, inplace=True)
    if used_columns:
        log.debug(
            'These columns are not dropped because present in used_as_input_variables:\n {}'
            .format(sorted(used_columns)))
    if dropped_columns:
        log.debug(
            """These columns in survey are set to be calculated, we drop them from the input table:
 {}"""
            .format(sorted(dropped_columns)))
    log.info('Keeping the following variables in the input_data_frame:\n {}'
        .format(sorted(list(input_data_frame.columns))))
    return input_data_frame