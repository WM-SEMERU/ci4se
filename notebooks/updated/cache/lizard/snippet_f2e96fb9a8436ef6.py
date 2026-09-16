def get_required(self, obj):
    required = []
    for field_name, field in sorted(obj.fields.items()):
        if field.required:
            required.append(field.name)
    return required or missing