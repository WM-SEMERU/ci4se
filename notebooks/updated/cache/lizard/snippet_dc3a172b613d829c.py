def all(cls, service_type=None, organisation_id=None, include_deactivated=False
    ):
    if include_deactivated:
        resources = yield views.services.get(key=[service_type,
            organisation_id])
    else:
        resources = yield views.active_services.get(key=[service_type,
            organisation_id])
    raise Return([cls(**resource['value']) for resource in resources['rows']])