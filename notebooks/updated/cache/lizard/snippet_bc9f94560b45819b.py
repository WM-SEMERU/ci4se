def register_standard(id, source_types, target_types, requirements=[]):
    g = Generator(id, False, source_types, target_types, requirements)
    register(g)
    return g