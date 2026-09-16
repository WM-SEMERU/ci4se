def import_units(module, namespace):
    for key, value in module.__dict__.items():
        if isinstance(value, (unyt_quantity, Unit)):
            namespace[key] = value