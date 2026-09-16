def get_domain_class_terminal_attribute_iterator(ent):
    for attr in itervalues_(ent.__everest_attributes__):
        if attr.kind == RESOURCE_ATTRIBUTE_KINDS.TERMINAL:
            yield attr