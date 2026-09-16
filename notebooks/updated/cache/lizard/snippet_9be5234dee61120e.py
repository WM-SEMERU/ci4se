def get_time_variable(ds):
    for var in ds.variables:
        if getattr(ds.variables[var], 'axis', '') == 'T':
            return var
    else:
        candidates = ds.get_variables_by_attributes(standard_name='time')
        if len(candidates) == 1:
            return candidates[0].name
        else:
            for candidate in candidates:
                if candidate.dimensions == (candidate.name,):
                    return candidate.name
    return None