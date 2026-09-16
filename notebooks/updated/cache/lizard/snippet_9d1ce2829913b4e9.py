def expandServices(service_elements):
    expanded = []
    for service_element in service_elements:
        expanded.extend(expandService(service_element))
    return expanded