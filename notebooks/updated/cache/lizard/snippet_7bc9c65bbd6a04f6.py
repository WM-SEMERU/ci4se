def _is_valid_service_url(url):
    valid_services = getattr(settings, 'MAMA_CAS_VALID_SERVICES', ())
    if not valid_services:
        return True
    warnings.warn(
        'The MAMA_CAS_VALID_SERVICES setting is deprecated. Services should be configured using MAMA_CAS_SERVICES.'
        , DeprecationWarning)
    for service in [re.compile(s) for s in valid_services]:
        if service.match(url):
            return True
    return False