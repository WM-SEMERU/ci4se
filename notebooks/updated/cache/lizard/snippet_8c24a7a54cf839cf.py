def get_displacement_rate(hazard, classification, hazard_class, qsettings=None
    ):
    is_affected_value = is_affected(hazard, classification, hazard_class,
        qsettings)
    if is_affected_value == not_exposed_class['key']:
        return 0
    elif not is_affected_value:
        return 0
    preference_data = setting('population_preference', default=
        generate_default_profile(), qsettings=qsettings)
    default_profile = generate_default_profile()
    default_displacement_rate_value = default_profile.get(hazard, {}).get(
        classification, {}).get(hazard_class, {}).get('displacement_rate', 0)
    return preference_data.get(hazard, {}).get(classification, {}).get(
        hazard_class, {}).get('displacement_rate',
        default_displacement_rate_value)