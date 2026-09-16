def _find_recursive_dependencies(sql, values, code, resolved_vars,
    resolving_vars=None):
    dependencies = SqlStatement._get_dependencies(sql)
    for dependency in dependencies:
        if dependency in resolved_vars:
            continue
        dep = datalab.utils.get_item(values, dependency)
        if isinstance(dep, types.ModuleType):
            dep = _utils.get_default_query_from_module(dep)
        if dep is None:
            raise Exception('Unsatisfied dependency $%s' % dependency)
        if isinstance(dep, SqlStatement):
            if resolving_vars is None:
                resolving_vars = []
            elif dependency in resolving_vars:
                raise Exception('Circular dependency in $%s' % dependency)
            resolving_vars.append(dependency)
            SqlStatement._find_recursive_dependencies(dep._sql, values,
                code, resolved_vars, resolving_vars)
            resolving_vars.pop()
            resolved_vars[dependency] = SqlStatement(dep._sql)
        else:
            resolved_vars[dependency] = dep