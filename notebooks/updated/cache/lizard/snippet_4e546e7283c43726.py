def validate(cls, **kwargs):
    errors = ValidationErrors()
    obj = cls()
    redis = cls.get_redis()
    for fieldname, field in obj.proxy:
        if not field.fillable:
            value = field.default
        else:
            try:
                value = field.validate(kwargs.get(fieldname), redis)
            except BadField as e:
                errors.append(e)
                continue
        setattr(obj, fieldname, value)
    for fieldname in dir(cls):
        rule = getattr(cls, fieldname)
        if hasattr(rule, '_is_validation_rule') and rule._is_validation_rule:
            try:
                rule(obj)
            except BadField as e:
                errors.append(e)
    if errors.has_errors():
        raise errors
    return obj