def temporary_instance_cache(*classes):
    orig_instances = []
    for cls in classes:
        orig_instances.append(cls._instances)
        cls._instances = {}
    try:
        yield
    finally:
        for i, cls in enumerate(classes):
            cls._instances = orig_instances[i]