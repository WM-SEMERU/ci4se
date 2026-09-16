def _validate_applications(self, apps):
    for application_id, application_config in apps.items():
        self._validate_config(application_id, application_config)
        application_config['APPLICATION_ID'] = application_id