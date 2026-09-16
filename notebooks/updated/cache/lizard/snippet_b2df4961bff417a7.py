def expand(self, repex_vars, fields):
    r
    logger.debug('Expanding variables...')
    unexpanded_instances = set()
    for k, v in repex_vars.items():
        repex_vars[k] = self._expand_var(v, repex_vars)
        instances = self._get_instances(repex_vars[k])
        unexpanded_instances.update(instances)
    for key in fields.keys():
        field = fields[key]
        if isinstance(field, str):
            fields[key] = self._expand_var(field, repex_vars)
            instances = self._get_instances(fields[key])
            unexpanded_instances.update(instances)
        elif isinstance(field, dict):
            for k, v in field.items():
                fields[key][k] = self._expand_var(v, repex_vars)
                instances = self._get_instances(fields[key][k])
                unexpanded_instances.update(instances)
        elif isinstance(field, list):
            for index, item in enumerate(field):
                fields[key][index] = self._expand_var(item, repex_vars)
                instances = self._get_instances(fields[key][index])
                unexpanded_instances.update(instances)
    if unexpanded_instances:
        raise RepexError(
            """Variables failed to expand: {0}
Please make sure to provide all necessary variables """
            .format(list(unexpanded_instances)))
    return fields