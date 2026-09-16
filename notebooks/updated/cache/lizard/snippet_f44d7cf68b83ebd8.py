def _analyze_indexed_fields(indexed_fields):
    result = {}
    for field_name in indexed_fields:
        if not isinstance(field_name, basestring):
            raise TypeError('Field names must be strings; got %r' % (
                field_name,))
        if '.' not in field_name:
            if field_name in result:
                raise ValueError('Duplicate field name %s' % field_name)
            result[field_name] = None
        else:
            head, tail = field_name.split('.', 1)
            if head not in result:
                result[head] = [tail]
            elif result[head] is None:
                raise ValueError('Field name %s conflicts with ancestor %s' %
                    (field_name, head))
            else:
                result[head].append(tail)
    return result