def _format_object(obj, format_type=None):
    if json_api_settings.FORMAT_KEYS is not None:
        return format_keys(obj, format_type)
    return format_field_names(obj, format_type)