def get_parameter_p_value_too_high_warning(model_type, model_params,
    parameter, p_value, maximum_p_value):
    warnings = []
    if p_value > maximum_p_value:
        data = {'{}_p_value'.format(parameter): p_value,
            '{}_maximum_p_value'.format(parameter): maximum_p_value}
        data.update(model_params)
        warnings.append(EEMeterWarning(qualified_name=
            'eemeter.caltrack_daily.{model_type}.{parameter}_p_value_too_high'
            .format(model_type=model_type, parameter=parameter),
            description=
            'Model fit {parameter} p-value is too high. Candidate model rejected.'
            .format(parameter=parameter), data=data))
    return warnings