def get_row(self, row):
    if isinstance(self.fields, dict):
        return dict([(key, text_type(value).format(**row) if RE_FORMATTED.
            match(value) else row[value]) for key, value in self.fields.
            items()])
    else:
        return [(text_type(field).format(**row) if RE_FORMATTED.match(field
            ) else row[field]) for field in self.fields]