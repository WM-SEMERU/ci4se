def bluemix(cls, vcap_services, instance_name=None, service_name=None, **kwargs
    ):
    service_name = service_name or 'cloudantNoSQLDB'
    try:
        service = CloudFoundryService(vcap_services, instance_name=
            instance_name, service_name=service_name)
    except CloudantException:
        raise CloudantClientException(103)
    if hasattr(service, 'iam_api_key'):
        return Cloudant.iam(service.username, service.iam_api_key, url=
            service.url, **kwargs)
    return Cloudant(service.username, service.password, url=service.url, **
        kwargs)