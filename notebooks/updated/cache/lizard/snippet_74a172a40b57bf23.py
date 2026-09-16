def all_inspections(obj):
    for name, callback in INSPECTIONS:
        result = callback(obj)
        if result:
            yield name, result