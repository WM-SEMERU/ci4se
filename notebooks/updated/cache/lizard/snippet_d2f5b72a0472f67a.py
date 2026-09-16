def derive_link_fields(self, context):
    if self.link_fields is not None:
        return self.link_fields
    else:
        link_fields = set()
        if self.fields:
            for field in self.fields:
                if field != 'is_active':
                    link_fields.add(field)
                    break
    return link_fields