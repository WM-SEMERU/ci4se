def check(timeout, consumer=None, producer=None):
    consumers, producers = consumer, producer
    config = load_config()
    endpoint = config.get('moksha.monitoring.socket')
    if not endpoint:
        raise click.ClickException(
            'No monitoring endpoint has been configured: please set "moksha.monitoring.socket"'
            )
    context = zmq.Context.instance()
    socket = context.socket(zmq.SUB)
    socket.set(zmq.RCVTIMEO, timeout * 1000)
    socket.subscribe(b'')
    socket.connect(endpoint)
    try:
        message = socket.recv_json()
    except zmq.error.Again:
        raise click.ClickException(
            'Failed to receive message from the monitoring endpoint ({e}) in {t} seconds.'
            .format(e=endpoint, t=timeout))
    if not consumers and not producers:
        click.echo('No consumers or producers specified so all will be shown.')
    else:
        missing = False
        uninitialized = False
        for messager_type, messagers in (('consumers', consumers), (
            'producers', producers)):
            active = {}
            for messager in message[messager_type]:
                active[messager['name']] = messager
            for messager in messagers:
                if messager not in active:
                    click.echo('"{m}" is not active!'.format(m=messager),
                        err=True)
                    missing = True
                elif active[messager]['initialized'] is not True:
                    click.echo('"{m}" is not initialized!'.format(m=
                        messager), err=True)
                    uninitialized = True
        if missing:
            raise click.ClickException(
                'Some consumers and/or producers are missing!')
        elif uninitialized:
            raise click.ClickException(
                'Some consumers and/or producers are uninitialized!')
        else:
            click.echo('All consumers and producers are active!')
    click.echo(json.dumps(message, indent=2, sort_keys=True))