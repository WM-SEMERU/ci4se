def get_total_degree_day_too_low_warning(model_type, balance_point,
    degree_day_type, avg_degree_days, period_days, minimum_total):
    warnings = []
    total_degree_days = (avg_degree_days * period_days).sum()
    if total_degree_days < minimum_total:
        warnings.append(EEMeterWarning(qualified_name=
            'eemeter.caltrack_daily.{model_type}.total_{degree_day_type}_too_low'
            .format(model_type=model_type, degree_day_type=degree_day_type),
            description=
            'Total {degree_day_type} below accepted minimum. Candidate fit not attempted.'
            .format(degree_day_type=degree_day_type.upper()), data={
            'total_{degree_day_type}'.format(degree_day_type=
            degree_day_type): total_degree_days,
            'total_{degree_day_type}_minimum'.format(degree_day_type=
            degree_day_type): minimum_total,
            '{degree_day_type}_balance_point'.format(degree_day_type=
            degree_day_type): balance_point}))
    return warnings