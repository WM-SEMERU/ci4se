def is_resource_class_collection_attribute(rc, attr_name):
    attr = get_resource_class_attribute(rc, attr_name)
    return attr.kind == RESOURCE_ATTRIBUTE_KINDS.COLLECTION