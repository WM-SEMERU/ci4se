def delete_custom_field(self, custom_field_key):
    custom_field_key = quote(custom_field_key, '')
    response = self._delete('/lists/%s/customfields/%s.json' % (self.
        list_id, custom_field_key))