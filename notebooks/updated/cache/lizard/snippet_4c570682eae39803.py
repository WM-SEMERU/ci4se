def get_readonly_fields(self, request, obj=None):
    if obj is None:
        return []
    return super(ExportAdmin, self).get_readonly_fields(request, obj)