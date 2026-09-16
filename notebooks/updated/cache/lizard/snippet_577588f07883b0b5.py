def normalize_fieldsets(fieldsets):
    result = []
    for name, options in fieldsets:
        result.append((name, normalize_dictionary(options)))
    return result