def transform(matches, framework, namespace, static_endpoint):
    transformed = []
    namespace = namespace + '/' if namespace else ''
    for attribute, elements in matches:
        for element in elements:
            asset_location = get_asset_location(element, attribute)
            sub_dict = {'static_endpoint': static_endpoint, 'namespace':
                namespace, 'asset_location': asset_location}
            transformed_string = frameworks[framework] % sub_dict
            res = attribute, element[attribute], transformed_string
            transformed.append(res)
    return transformed