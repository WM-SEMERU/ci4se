def range_is_obj(rng, rdfclass):
    if rng == 'rdfs_Literal':
        return False
    if hasattr(rdfclass, rng):
        mod_class = getattr(rdfclass, rng)
        for item in mod_class.cls_defs['rdf_type']:
            try:
                if issubclass(getattr(rdfclass, item), rdfclass.rdfs_Literal):
                    return False
            except AttributeError:
                pass
        if isinstance(mod_class, rdfclass.RdfClassMeta):
            return True
    return False