def to_json(el, schema=None):
    if type(el) is str:
        json_el = el
    elif type(el) is list:
        json_el = list(map(to_json, el))
    elif type(el) is dict:
        assert 'tagName' in el
        json_el = el.copy()
        if 'attributes' not in el:
            json_el['attributes'] = {}
        if 'children' not in el:
            json_el['children'] = []
    elif isinstance(el, VDOM):
        json_el = el.to_dict()
    else:
        json_el = el
    if schema:
        try:
            validate(instance=json_el, schema=schema, cls=Draft4Validator)
        except ValidationError as e:
            raise ValidationError(_validate_err_template.format(schema, e))
    return json_el