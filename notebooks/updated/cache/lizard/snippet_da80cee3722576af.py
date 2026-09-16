def _convert_to_dictionary(obj):
    if isinstance(obj, list):
        return [Serializable._convert_to_dictionary(i) for i in obj]
    elif hasattr(obj, 'as_dictionary'):
        return obj.as_dictionary()
    else:
        return obj