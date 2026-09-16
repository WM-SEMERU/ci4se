def get_file_fields():
    all_models = apps.get_models()
    fields = []
    for model in all_models:
        for field in model._meta.get_fields():
            if isinstance(field, models.FileField):
                fields.append(field)
    return fields