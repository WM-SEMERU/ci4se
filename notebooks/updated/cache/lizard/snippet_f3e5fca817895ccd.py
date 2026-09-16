def table_schema_call(self, target, cls):
    index_defs = []
    for name in (cls.index_names() or []):
        index_defs.append(GlobalIncludeIndex(gsi_name(name), parts=[HashKey
            (name)], includes=['value']))
    return target(cls.get_table_name(), connection=get_conn(), schema=[
        HashKey('id')], global_indexes=index_defs or None)