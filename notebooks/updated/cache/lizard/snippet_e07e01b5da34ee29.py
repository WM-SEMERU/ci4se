def service_delete(service_id=None, name=None, profile=None, **connection_args
    ):
    kstone = auth(profile, **connection_args)
    if name:
        service_id = service_get(name=name, profile=profile, **connection_args
            )[name]['id']
    kstone.services.delete(service_id)
    return 'Keystone service ID "{0}" deleted'.format(service_id)