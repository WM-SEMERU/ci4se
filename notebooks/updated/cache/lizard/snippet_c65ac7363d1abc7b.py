def create_custom_field(self, field_name, data_type, options=[],
    visible_in_preference_center=True):
    body = {'FieldName': field_name, 'DataType': data_type, 'Options':
        options, 'VisibleInPreferenceCenter': visible_in_preference_center}
    response = self._post(self.uri_for('customfields'), json.dumps(body))
    return json_to_py(response)