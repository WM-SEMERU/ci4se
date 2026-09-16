def validate_service(self, request, uid):
    spec_min = get_record_value(request, uid, 'min')
    spec_max = get_record_value(request, uid, 'max')
    error = get_record_value(request, uid, 'error', '0')
    warn_min = get_record_value(request, uid, 'warn_min')
    warn_max = get_record_value(request, uid, 'warn_max')
    if not spec_min and not spec_max:
        return None
    if not api.is_floatable(spec_min):
        return "'Min' value must be numeric"
    if not api.is_floatable(spec_max):
        return "'Max' value must be numeric"
    if api.to_float(spec_min) > api.to_float(spec_max):
        return "'Max' value must be above 'Min' value"
    if not api.is_floatable(error) or 0.0 < api.to_float(error) > 100:
        return '% Error must be between 0 and 100'
    if warn_min:
        if not api.is_floatable(warn_min):
            return "'Warn Min' value must be numeric or empty"
        if api.to_float(warn_min) > api.to_float(spec_min):
            return "'Warn Min' value must be below 'Min' value"
    if warn_max:
        if not api.is_floatable(warn_max):
            return "'Warn Max' value must be numeric or empty"
        if api.to_float(warn_max) < api.to_float(spec_max):
            return "'Warn Max' value must be above 'Max' value"
    return None