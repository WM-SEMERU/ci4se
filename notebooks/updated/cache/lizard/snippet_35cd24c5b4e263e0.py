async def create(cls, *, type: str, power_address: str, power_user: str=
    None, power_pass: str=None, name: str=None, zone: typing.Union[str,
    Zone]=None, tags: typing.Sequence[str]=None):
    params = remove_None({'type': type, 'power_address': power_address,
        'power_user': power_user, 'power_pass': power_pass, 'name': name,
        'tags': tags})
    if type == 'rsd' and power_user is None:
        message = "'power_user' is required for pod type `rsd`"
        raise OperationNotAllowed(message)
    if type == 'rsd' and power_pass is None:
        message = "'power_pass' is required for pod type `rsd`"
        raise OperationNotAllowed(message)
    if zone is not None:
        if isinstance(zone, Zone):
            params['zone'] = zone.name
        elif isinstance(zone, str):
            params['zone'] = zone
        else:
            raise TypeError('zone must be a str or Zone, not %s' % type(
                zone).__name__)
    return cls._object(await cls._handler.create(**params))