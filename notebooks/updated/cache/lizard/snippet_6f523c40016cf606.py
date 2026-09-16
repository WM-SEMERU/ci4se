def get_readonly_fields(self, request, obj=None):
    return list(self.readonly_fields) + [field.name for field in obj._meta.
        fields]