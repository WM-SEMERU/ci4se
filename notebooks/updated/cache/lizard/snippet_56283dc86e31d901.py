def get_resource_listing(url, offset, limit, properties):
    query = [QPARA_OFFSET + '=' + str(offset), QPARA_LIMIT + '=' + str(limit)]
    if not properties is None:
        if len(properties) > 0:
            query.append(QPARA_ATTRIBUTES + '=' + ','.join(properties))
    url = url + '?' + '&'.join(query)
    json_obj = JsonResource(url).json
    resources = []
    for element in json_obj['items']:
        resource = ResourceHandle(element)
        if not properties is None:
            resource.properties = {}
            for prop in properties:
                if prop in element:
                    resource.properties[prop] = element[prop]
        resources.append(resource)
    return resources