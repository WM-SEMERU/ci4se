def inflate(cls, rel):
    props = {}
    for key, prop in cls.defined_properties(aliases=False, rels=False).items():
        if key in rel:
            props[key] = prop.inflate(rel[key], obj=rel)
        elif prop.has_default:
            props[key] = prop.default_value()
        else:
            props[key] = None
    srel = cls(**props)
    srel._start_node_id = rel.start_node.id
    srel._end_node_id = rel.end_node.id
    srel.id = rel.id
    return srel