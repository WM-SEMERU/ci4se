def serialize_instance(instance):
    data = {}
    for k, v in instance.__dict__.items():
        if k.startswith('_') or callable(v):
            continue
        try:
            field = instance._meta.get_field(k)
            if isinstance(field, BinaryField):
                v = force_str(base64.b64encode(v))
            elif isinstance(field, FileField):
                if v and not isinstance(v, six.string_types):
                    v = v.name
            try:
                json.dumps(v, cls=DjangoJSONEncoder)
            except TypeError:
                v = field.get_prep_value(v)
                k = SERIALIZED_DB_FIELD_PREFIX + k
        except FieldDoesNotExist:
            pass
        data[k] = v
    return json.loads(json.dumps(data, cls=DjangoJSONEncoder))