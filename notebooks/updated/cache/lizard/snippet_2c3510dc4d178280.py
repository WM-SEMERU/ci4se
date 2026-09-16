def filter_components_by_name(name, components_list, type_=T_RPM):
    for components in components_list:
        for component in components:
            if component['type'] == type_ and component['name'] == name:
                yield component