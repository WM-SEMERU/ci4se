def service_create(name, service_type, description=None, profile=None, **
    connection_args):
    kstone = auth(profile, **connection_args)
    service = kstone.services.create(name, service_type, description=
        description)
    return service_get(service.id, profile=profile, **connection_args)