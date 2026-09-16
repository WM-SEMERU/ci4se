def create_content_type(json):
    result = ContentType(json['sys'])
    for field in json['fields']:
        field_id = field['id']
        del field['id']
        result.fields[field_id] = field
    result.name = json['name']
    result.display_field = json.get('displayField')
    return result