def _can_process_application(self, app):
    return self.LOCATION_KEY in app.properties and isinstance(app.
        properties[self.LOCATION_KEY], dict
        ) and self.APPLICATION_ID_KEY in app.properties[self.LOCATION_KEY
        ] and self.SEMANTIC_VERSION_KEY in app.properties[self.LOCATION_KEY]