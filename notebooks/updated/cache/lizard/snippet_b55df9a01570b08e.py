def service_name(doc):
    for service_id, service in doc.get('services', {}).items():
        service['id'] = service_id
        service['organisation_id'] = doc['_id']
        name = service.get('name', None)
        if name:
            yield name, service