def users_create(identity, password, active):
    kwargs = {attr: identity for attr in _security.user_identity_attributes}
    kwargs.update(**{'password': password, 'active': 'y' if active else ''})
    form = _security.confirm_register_form(MultiDict(kwargs), meta={'csrf':
        False})
    if form.validate():
        kwargs['password'] = hash_password(kwargs['password'])
        kwargs['active'] = active
        _datastore.create_user(**kwargs)
        click.secho('User created successfully.', fg='green')
        kwargs['password'] = '****'
        click.echo(kwargs)
    else:
        raise click.UsageError('Error creating user. %s' % form.errors)