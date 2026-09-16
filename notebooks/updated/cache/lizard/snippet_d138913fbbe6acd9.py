def record_factory(app, fields=None):
    record = Record(app, {'$type': Record._type, 'isNew': True,
        'applicationId': app.id, 'comments': {'$type':
        'System.Collections.Generic.Dictionary`2[[System.String, mscorlib],[System.Collections.Generic.List`1[[Core.Models.Record.Comments, Core]], mscorlib]], mscorlib'
        }, 'values': {'$type':
        'System.Collections.Generic.Dictionary`2[[System.String, mscorlib],[System.Object, mscorlib]], mscorlib'
        }})
    fields = fields or {}
    for name, value in six.iteritems(fields):
        record[name] = value
    copy_raw = copy.copy(record._raw)
    values_dict = {}
    for key, value in six.iteritems(copy_raw['values']):
        if value is not None:
            values_dict[key] = value
    record._raw['values'] = values_dict
    return record