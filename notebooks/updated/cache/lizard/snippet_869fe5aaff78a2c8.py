def make_schema(fields, datefields=()):
    text_field = whoosh.fields.TEXT(analyzer=whoosh.analysis.SimpleAnalyzer())
    fields = dict.fromkeys(fields, text_field)
    if datefields:
        datefields = dict.fromkeys(datefields, whoosh.fields.DATETIME)
        fields.update(datefields)
    schema = whoosh.fields.Schema()
    for fieldname in fields:
        schema.add(fieldname, fields[fieldname])
    return schema