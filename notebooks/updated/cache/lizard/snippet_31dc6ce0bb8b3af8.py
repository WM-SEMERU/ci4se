def insert_enum_option(self, custom_field, params={}, **options):
    path = '/custom_fields/%s/enum_options/insert' % custom_field
    return self.client.post(path, params, **options)