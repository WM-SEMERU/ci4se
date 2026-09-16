def geo_field(queryset):
    for field in queryset.model._meta.fields:
        if isinstance(field, models.GeometryField):
            return field
    raise exceptions.FieldDoesNotExist('No GeometryField found')