def validate_extension(self, file_name, extension_map, method_title,
    argument_title):
    title = 'validate_extension'
    ext_arg = '%s(extension_map={...})' % title
    input_fields = {'file_name': file_name, 'method_title': method_title,
        'argument_title': argument_title}
    for key, value in input_fields.items():
        if not isinstance(value, str):
            raise ValueError('%s(%s="...") must be a string' % (title, key))
    if not isinstance(extension_map, dict):
        raise ValueError('%s must be a dictionary.' % ext_arg)
    import re
    file_details = {'mimetype': '', 'extension': ''}
    type_list = []
    for key, value in extension_map.items():
        if not isinstance(value, dict):
            raise ValueError('%s %s key must be a dictionary.' % (ext_arg, key)
                )
        elif not 'extension' in value.keys():
            raise ValueError('%s %s dict must have an "extension" key.' % (
                ext_arg, key))
        type_list.append(value['extension'])
        regex_pattern = re.compile(key)
        if regex_pattern.findall(file_name):
            file_details.update(**value)
    if not file_details['extension']:
        raise ValueError('%s(%s=%s) must be one of %s extension types.' % (
            method_title, argument_title, file_name, type_list))
    return file_details