def parse_schema(schema, _write_hint=True, _force=False):
    if _force:
        return _parse_schema(schema, '', _write_hint)
    elif isinstance(schema, dict) and '__fastavro_parsed' in schema:
        return schema
    else:
        return _parse_schema(schema, '', _write_hint)