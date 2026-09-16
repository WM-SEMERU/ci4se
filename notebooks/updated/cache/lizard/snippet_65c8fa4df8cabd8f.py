def _parse_options(self, options):
    for key in ('username', 'client_name', 'client_id', 'client_secret',
        'trusted', 'logout_uri'):
        value = options.get(key)
        if value is not None:
            self.fields[key] = value
    username = self.fields.pop('username', None)
    if username is not None:
        try:
            user_model = get_user_model()
            self.fields['user'] = user_model.objects.get(username=username)
        except user_model.DoesNotExist:
            raise CommandError(
                'User matching the provided username does not exist.')
    client_name = self.fields.pop('client_name', None)
    if client_name is not None:
        self.fields['name'] = client_name
    logout_uri = self.fields.get('logout_uri')
    if logout_uri:
        try:
            URLValidator()(logout_uri)
        except ValidationError:
            raise CommandError('The logout_uri is invalid.')