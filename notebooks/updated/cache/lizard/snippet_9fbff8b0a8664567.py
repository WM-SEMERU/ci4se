def describe_field(k, v, timestamp_parser=default_timestamp_parser):

    def bq_schema_field(name, bq_type, mode):
        return {'name': name, 'type': bq_type, 'mode': mode}
    if isinstance(v, list):
        if len(v) == 0:
            raise Exception(
                "Can't describe schema because of empty list {0}:[]".format(k))
        v = v[0]
        mode = 'repeated'
    else:
        mode = 'nullable'
    bq_type = bigquery_type(v, timestamp_parser=timestamp_parser)
    if not bq_type:
        raise InvalidTypeException(k, v)
    field = bq_schema_field(k, bq_type, mode)
    if bq_type == 'record':
        try:
            field['fields'] = schema_from_record(v, timestamp_parser)
        except InvalidTypeException as e:
            raise InvalidTypeException('%s.%s' % (k, e.key), e.value)
    return field