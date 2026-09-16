def import_class_by_string(name):
    components = name.split('.')
    clazz = components.pop()
    mod = __import__('.'.join(components))
    components += [clazz]
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod