def _validate_required_settings(self, application_id, application_config,
    required_settings):
    for setting_key in required_settings:
        if setting_key not in application_config.keys():
            raise ImproperlyConfigured(MISSING_SETTING.format(
                application_id=application_id, setting=setting_key))