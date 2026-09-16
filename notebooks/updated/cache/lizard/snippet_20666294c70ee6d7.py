async def set_permissions(self, target, *, overwrite=_undefined, reason=
    None, **permissions):
    r
    http = self._state.http
    if isinstance(target, User):
        perm_type = 'member'
    elif isinstance(target, Role):
        perm_type = 'role'
    else:
        raise InvalidArgument('target parameter must be either Member or Role')
    if isinstance(overwrite, _Undefined):
        if len(permissions) == 0:
            raise InvalidArgument('No overwrite provided.')
        try:
            overwrite = PermissionOverwrite(**permissions)
        except (ValueError, TypeError):
            raise InvalidArgument(
                'Invalid permissions given to keyword arguments.')
    elif len(permissions) > 0:
        raise InvalidArgument('Cannot mix overwrite and keyword arguments.')
    if overwrite is None:
        await http.delete_channel_permissions(self.id, target.id, reason=reason
            )
    elif isinstance(overwrite, PermissionOverwrite):
        allow, deny = overwrite.pair()
        await http.edit_channel_permissions(self.id, target.id, allow.value,
            deny.value, perm_type, reason=reason)
    else:
        raise InvalidArgument('Invalid overwrite type provided.')