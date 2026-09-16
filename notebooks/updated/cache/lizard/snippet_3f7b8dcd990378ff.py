def validate_config_parameters(config_json, allowed_keys, allowed_types):
    custom_fields = config_json.get(defs.PARAMETERS, [])
    for field in custom_fields:
        validate_field(field, allowed_keys, allowed_types)
        default = field.get(defs.DEFAULT)
        field_type = field.get(defs.TYPE)
        if default:
            validate_field_matches_type(field[defs.VALUE], default, field_type)