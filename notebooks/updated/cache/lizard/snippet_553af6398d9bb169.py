def _add_not_exposed(analysis_row, enable_rounding, is_population,
    exposure_unit, coefficient):
    not_exposed_field = hazard_count_field['field_name'] % not_exposed_class[
        'key']
    try:
        value = analysis_row[not_exposed_field]
    except KeyError:
        value = 0
    value = format_number(value, enable_rounding, is_population, coefficient)
    label = _format_label(hazard_class=not_exposed_class['name'], value=
        value, exposure_unit=exposure_unit)
    return not_exposed_class['color'], label