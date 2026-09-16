def check_fieldsets(*args, **kwargs):
    if hasattr(settings, 'CONFIG_FIELDSETS') and settings.CONFIG_FIELDSETS:
        inconsistent_fieldnames = get_inconsistent_fieldnames()
        if inconsistent_fieldnames:
            return [checks.Warning(_(
                'CONSTANCE_CONFIG_FIELDSETS is missing field(s) that exists in CONSTANCE_CONFIG.'
                ), hint=', '.join(sorted(inconsistent_fieldnames)), obj=
                'settings.CONSTANCE_CONFIG', id='constance.E001')]
    return []