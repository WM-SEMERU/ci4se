def _convert_old_schema(self, parameters):
    merged = []
    for parameter in parameters:
        segments = parameter.name.split('.')
        _merge_associative_list(merged, segments, parameter)
    result = [self._inner_convert_old_schema(node, 1) for node in merged]
    return result