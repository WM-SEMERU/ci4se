def import_from_string(value):
    value = value.replace('-', '_')
    try:
        module_path, class_name = value.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, class_name)
    except (ImportError, AttributeError) as ex:
        raise ImportError("Could not import '{}'. {}: {}.".format(value, ex
            .__class__.__name__, ex))