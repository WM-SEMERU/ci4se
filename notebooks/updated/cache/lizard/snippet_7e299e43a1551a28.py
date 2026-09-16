def update_custom_field(self, custom_field_key, field_name,
    visible_in_preference_center):
    custom_field_key = quote(custom_field_key, '')
    body = {'FieldName': field_name, 'VisibleInPreferenceCenter':
        visible_in_preference_center}
    response = self._put(self.uri_for('customfields/%s' % custom_field_key),
        json.dumps(body))
    return json_to_py(response)