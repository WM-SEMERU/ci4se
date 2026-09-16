def namedb_find_missing_and_extra(cur, record, table_name):
    rec_missing = []
    rec_extra = []
    name_fields_rows = db_query_execute(cur, 'PRAGMA table_info({})'.format
        (table_name), ())
    name_fields = []
    for row in name_fields_rows:
        name_fields.append(row['name'])
    for f in name_fields:
        if f not in record.keys():
            rec_missing.append(f)
    for k in record.keys():
        if k not in name_fields:
            rec_extra.append(k)
    return rec_missing, rec_extra