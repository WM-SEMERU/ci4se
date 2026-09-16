def _get_object(class_, obj):
    if isinstance(obj, list):
        return [Serializable._get_object(class_, i) for i in obj]
    elif isinstance(obj, dict):
        return class_(**keys_to_snake_case(obj))
    else:
        return obj