def session_hook(exception):
    safeprint(
        'The resource you are trying to access requires you to re-authenticate with specific identities.'
        )
    params = exception.raw_json['authorization_parameters']
    message = params.get('session_message')
    if message:
        safeprint('message: {}'.format(message))
    identities = params.get('session_required_identities')
    if identities:
        id_str = ' '.join(identities)
        safeprint(
            """Please run

    globus session update {}

to re-authenticate with the required identities"""
            .format(id_str))
    else:
        safeprint(
            'Please use "globus session update" to re-authenticate with specific identities'
            .format(id_str))
    exit_with_mapped_status(exception.http_status)