def _create_or_update_user(self, create, name, password, read_only, **kwargs):
    opts = {}
    if read_only or create and 'roles' not in kwargs:
        warnings.warn(
            'Creating a user with the read_only option or without roles is deprecated in MongoDB >= 2.6'
            , DeprecationWarning)
        opts['roles'] = [self._default_role(read_only)]
    elif read_only:
        warnings.warn(
            "The read_only option is deprecated in MongoDB >= 2.6, use 'roles' instead"
            , DeprecationWarning)
    if password is not None:
        if 'digestPassword' in kwargs:
            raise ConfigurationError(
                "The digestPassword option is not supported via add_user. Please use db.command('createUser', ...) instead for this option."
                )
        opts['pwd'] = auth._password_digest(name, password)
        opts['digestPassword'] = False
    if self.write_concern.acknowledged and self.write_concern.document:
        opts['writeConcern'] = self.write_concern.document
    opts.update(kwargs)
    if create:
        command_name = 'createUser'
    else:
        command_name = 'updateUser'
    self.command(command_name, name, **opts)