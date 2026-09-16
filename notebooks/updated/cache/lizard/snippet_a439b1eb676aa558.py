def has_documented_fields(self, include_inherited_fields=False):
    fields = self.all_fields if include_inherited_fields else self.fields
    for field in fields:
        if field.doc:
            return True
    return False