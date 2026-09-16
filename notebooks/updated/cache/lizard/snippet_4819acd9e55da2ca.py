def save_to_db(model_text_id, parsed_values):
    Model = apps.get_model(model_text_id)
    simple_fields = {}
    many2many_fields = {}
    for field, value in parsed_values.items():
        if Model._meta.get_field(field).get_internal_type(
            ) == 'ManyToManyField':
            many2many_fields[field] = value
        elif Model._meta.get_field(field).get_internal_type(
            ) == 'DateTimeField':
            simple_fields[field] = time_parser.parse(value)
        else:
            simple_fields[field] = value
    model, created = Model.objects.get_or_create(**simple_fields)
    for field, value in many2many_fields.items():
        setattr(model, field, value)
    model.save()
    return model