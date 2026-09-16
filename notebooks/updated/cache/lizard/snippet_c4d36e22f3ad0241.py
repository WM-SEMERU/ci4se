def import_from_json(filename_or_fobj, encoding='utf-8', *args, **kwargs):
    source = Source.from_file(filename_or_fobj, mode='rb', plugin_name=
        'json', encoding=encoding)
    json_obj = json.load(source.fobj, encoding=source.encoding)
    field_names = list(json_obj[0].keys())
    table_rows = [[item[key] for key in field_names] for item in json_obj]
    meta = {'imported_from': 'json', 'source': source}
    return create_table([field_names] + table_rows, *args, meta=meta, **kwargs)