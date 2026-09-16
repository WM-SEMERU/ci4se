def update_enum_option(self, enum_option, params={}, **options):
    path = '/enum_options/%s' % enum_option
    return self.client.put(path, params, **options)