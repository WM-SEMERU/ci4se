def convert_general(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, list):
        value = [convert_general(item) for item in value]
        value = convert_to_imgur_list(value)
    elif isinstance(value, Integral):
        return str(value)
    elif 'pyimgur' in str(type(value)):
        return str(getattr(value, 'id', value))
    return value