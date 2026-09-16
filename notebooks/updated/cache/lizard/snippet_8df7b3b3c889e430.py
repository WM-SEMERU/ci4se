def _is_visible(cls, property_name):
    if isinstance(property_name, list):
        return [cls._is_visible(p) for p in property_name]
    if property_name.startswith('__') and property_name.endswith('__'):
        return False
    return property_name.startswith(cls.STARTS_WITH
        ) and property_name.endswith(cls.ENDS_WITH)