def _create_service(client, organisation_id, name, location, service_type):
    try:
        response = client.accounts.organisations[organisation_id
            ].services.post(name=name, location=location, service_type=
            service_type)
        service_id = response['data']['id']
    except httpclient.HTTPError as exc:
        if exc.code == 404:
            msg = (
                'Organisation {} cannot be found. Please check organisation_id.'
                .format(organisation_id))
            raise click.ClickException(click.style(msg, fg='red'))
        else:
            service_id = _get_service(client, organisation_id, name)
            if not service_id:
                raise exc
    return service_id