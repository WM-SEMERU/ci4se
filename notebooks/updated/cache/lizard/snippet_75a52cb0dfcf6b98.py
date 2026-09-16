def unicode_convert(obj):
    try:
        if isinstance(obj, dict):
            return {unicode_convert(key): unicode_convert(value) for key,
                value in obj.items()}
        elif isinstance(obj, list):
            return [unicode_convert(element) for element in obj]
        elif isinstance(obj, str):
            return obj
        elif isinstance(obj, six.text_type):
            return obj.encode('utf-8')
        elif isinstance(obj, six.integer_types):
            return obj
        else:
            return obj
    except:
        return obj