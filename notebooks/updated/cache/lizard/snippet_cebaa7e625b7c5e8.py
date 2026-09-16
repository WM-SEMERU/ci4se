def create(image, name=None, start=False, skip_translate=None,
    ignore_collisions=False, validate_ip_addrs=True, client_timeout=salt.
    utils.docker.CLIENT_TIMEOUT, **kwargs):
    if kwargs.pop('inspect', True) and not resolve_image_id(image):
        pull(image, client_timeout=client_timeout)
    kwargs, unused_kwargs = _get_create_kwargs(skip_translate=
        skip_translate, ignore_collisions=ignore_collisions,
        validate_ip_addrs=validate_ip_addrs, **kwargs)
    if unused_kwargs:
        log.warning(
            'The following arguments were ignored because they are not recognized by docker-py: %s'
            , sorted(unused_kwargs))
    log.debug(
        'docker.create: creating container %susing the following arguments: %s'
        , "with name '{0}' ".format(name) if name is not None else '', kwargs)
    time_started = time.time()
    response = _client_wrapper('create_container', image, name=name, **kwargs)
    response['Time_Elapsed'] = time.time() - time_started
    _clear_context()
    if name is None:
        name = inspect_container(response['Id'])['Name'].lstrip('/')
    response['Name'] = name
    if start:
        try:
            start_(name)
        except CommandExecutionError as exc:
            raise CommandExecutionError(
                'Failed to start container after creation', info={
                'response': response, 'error': exc.__str__()})
        else:
            response['Started'] = True
    return response