def field_set(doc, field, value):
    if value is None:
        doc.__delitem__(field)
    else:
        doc[field] = value