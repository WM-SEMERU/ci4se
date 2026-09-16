def get_resources(cls):
    my_plurals = resource_helper.build_plural_mappings({},
        RESOURCE_ATTRIBUTE_MAP)
    attributes.PLURALS.update(my_plurals)
    attr_map = RESOURCE_ATTRIBUTE_MAP
    ext_resources = resource_helper.build_resource_info(my_plurals,
        attr_map, constants.A10_CERTIFICATE)
    return ext_resources