def rule_collection(href, cls):
    instance = cls(href=href)
    meth = getattr(instance, 'create')
    return type(cls.__name__, (SubElementCollection,), {'create': meth,
        'create_rule_section': instance.create_rule_section})(href, cls)