def filename_formatters(self, data, row):
    r = {'source': data.get('source'), 'field': self.field, 'type': data.
        get('type')}
    r.update(**row)
    return r