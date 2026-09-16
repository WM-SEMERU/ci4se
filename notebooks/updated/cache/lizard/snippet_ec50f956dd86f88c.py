def get_variable_accesses(self, variable, same_name=False):
    if variable.region == 'global':
        return self.global_manager.get_variable_accesses(variable,
            same_name=same_name)
    elif variable.region in self.function_managers:
        return self.function_managers[variable.region].get_variable_accesses(
            variable, same_name=same_name)
    l.warning('get_variable_accesses(): Region %s is not found.', variable.
        region)
    return []